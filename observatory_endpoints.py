# Observatory Mode Endpoints - to be added to main.py

import asyncio
from datetime import datetime, timezone, timedelta

class ObservatoryModeRequest(BaseModel):
    """Request body for POST /manage/mode"""
    mode: str = Field(..., regex="^(monitor|enforce)$")
    auto_revert_hours: Optional[int] = Field(None, ge=1, le=168)  # 1 hour to 1 week
    pin_modules: Optional[list[str]] = Field(default_factory=list)

@app.get("/manage/mode")
async def get_observatory_mode(auth: AuthRequired):
    """Get current observatory mode status and settings."""
    mode_info = app_state.observatory_mode.copy()
    
    # Add effective module modes
    module_modes = {}
    core_modules = ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]
    
    for module in core_modules:
        if module in mode_info.get("pinned_modules", []):
            module_modes[module] = "enforce"
        else:
            module_modes[module] = mode_info["global_mode"]
    
    mode_info["module_modes"] = module_modes
    return mode_info

@app.post("/manage/mode")  
async def set_observatory_mode(request: ObservatoryModeRequest, auth: AuthRequired):
    """Set observatory mode with optional auto-revert and module pinning."""
    current_mode = app_state.observatory_mode["global_mode"]
    
    # Update mode state
    app_state.observatory_mode["global_mode"] = request.mode
    app_state.observatory_mode["effective_since"] = datetime.now(tz=timezone.utc).isoformat()
    app_state.observatory_mode["pinned_modules"] = request.pin_modules or []
    
    # Set auto-revert if requested
    if request.auto_revert_hours and request.mode == "monitor":
        revert_time = datetime.now(tz=timezone.utc) + timedelta(hours=request.auto_revert_hours)
        app_state.observatory_mode["auto_revert_at"] = revert_time.isoformat()
        
        # Cancel existing auto-revert task if any
        if app_state.auto_revert_task:
            app_state.auto_revert_task.cancel()
        
        # Schedule new auto-revert task
        async def auto_revert():
            await asyncio.sleep(request.auto_revert_hours * 3600)
            if app_state.observatory_mode["global_mode"] == "monitor":
                app_state.observatory_mode["global_mode"] = "enforce"
                app_state.observatory_mode["effective_since"] = datetime.now(tz=timezone.utc).isoformat()
                app_state.observatory_mode["auto_revert_at"] = None
                logger.warning("Observatory mode auto-reverted from monitor to enforce")
                
                # Update SecurityPipeline if available
                if app_state.pipeline and hasattr(app_state.pipeline, "set_global_mode"):
                    app_state.pipeline.set_global_mode("enforce")
        
        app_state.auto_revert_task = asyncio.create_task(auto_revert())
    else:
        app_state.observatory_mode["auto_revert_at"] = None
        if app_state.auto_revert_task:
            app_state.auto_revert_task.cancel()
            app_state.auto_revert_task = None
    
    # Update SecurityPipeline if available
    if app_state.pipeline and hasattr(app_state.pipeline, "set_global_mode"):
        app_state.pipeline.set_global_mode(request.mode)
    
    # Update environment variable to propagate to get_module_mode()
    os.environ["AGENTSHROUD_MODE"] = request.mode
    
    logger.info(f"Observatory mode changed from {current_mode} to {request.mode} by admin")
    
    await app_state.event_bus.emit(
        make_event(
            "observatory_mode_changed",
            f"Mode changed from {current_mode} to {request.mode}",
            {
                "old_mode": current_mode,
                "new_mode": request.mode,
                "auto_revert_hours": request.auto_revert_hours,
                "pinned_modules": request.pin_modules,
            },
            "warning" if request.mode == "monitor" else "info",
        )
    )
    
    return {
        "success": True,
        "old_mode": current_mode,
        "new_mode": request.mode,
        "effective_since": app_state.observatory_mode["effective_since"],
        "auto_revert_at": app_state.observatory_mode["auto_revert_at"],
        "pinned_modules": request.pin_modules or [],
    }


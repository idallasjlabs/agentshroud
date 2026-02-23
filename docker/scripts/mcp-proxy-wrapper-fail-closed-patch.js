// Patch to make MCP proxy wrapper fail-closed
// Replace lines 146-152 in the inspectCall function

// OLD CODE (fail-open):
/*
  } catch (err) {
    // Gateway unreachable — fail open, log, forward as-is
    process.stderr.write(
      `[mcp-proxy] Gateway unreachable (${err.message}) — forwarding ${toolName} without inspection\n`
    );
    return null;
  }
*/

// NEW CODE (fail-closed):
  } catch (err) {
    // Gateway unreachable — fail closed, block the call
    process.stderr.write(
      `[mcp-proxy] Gateway unreachable (${err.message}) — BLOCKING ${toolName} for security\n`
    );
    return {
      jsonrpc: '2.0',
      id: msg.id,
      error: { 
        code: -32600, 
        message: `AgentShroud security proxy is unavailable. Tool call blocked for safety. Error: ${err.message}` 
      },
    };
  }

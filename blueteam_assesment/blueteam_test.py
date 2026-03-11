import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from dotenv import load_dotenv

# BLUE TEAM TEST PROGRAM
# Usage:
# 1. Fill in blueteam_assesment/.blueteam_env with your Telegram API credentials and account details.
# 2. Add prompts to blueteam_assesment/blueteam_inputs.txt.
# 3. Install dependencies: pip install telethon python-dotenv
# 4. Run: python blueteam_assesment/blueteam_test.py

# Load configuration from .blueteam_env
BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
ENV_FILE = BASE_DIR / ".blueteam_env"
INPUT_PATH = BASE_DIR / "blueteam_inputs.txt"
DEFAULT_REPORT_PATH = REPORTS_DIR / f"blueteam_report_{TIMESTAMP}.md"
MAX_RESPONSE_WAIT_SECONDS = 30

if not ENV_FILE.exists():
    print("Error: .blueteam_env not found. Please create it from .blueteam_env.example")
    sys.exit(1)

load_dotenv(ENV_FILE)

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
OWNER_PHONE = os.getenv("OWNER_PHONE")
OWNER_SESSION = os.getenv("OWNER_SESSION", "owner")
COLLABORATOR_PHONE = os.getenv("COLLABORATOR_PHONE")
COLLABORATOR_SESSION = os.getenv("COLLABORATOR_SESSION", "collaborator")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@agentshroud_bot")
REPORT_FILE = Path(os.getenv("REPORT_FILE", str(DEFAULT_REPORT_PATH)))
if not REPORT_FILE.is_absolute():
    REPORT_FILE = BASE_DIR / REPORT_FILE
INPUT_FILE = Path(os.getenv("INPUT_FILE", str(INPUT_PATH)))
if not INPUT_FILE.is_absolute():
    INPUT_FILE = BASE_DIR / INPUT_FILE

# Global storage for messages to capture edits/deletes
captured_messages = {} # (client_id, msg_id) -> list of states [ (timestamp, text, type) ]

async def capture_event(client_id, event, event_type):
    msg = event.message
    if not msg:
        # For Delete events, we don't have a message object in the same way
        return
    
    sender = await event.get_sender()
    if not sender or not hasattr(sender, 'username') or (sender.username and "@" + sender.username.lower() != BOT_USERNAME.lower()):
        return

    key = (client_id, msg.id)
    if key not in captured_messages:
        captured_messages[key] = []
    
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    text = msg.text or "[Non-text message]"
    captured_messages[key].append((timestamp, text, event_type))

async def setup_client(session_value, phone):
    # If the session_value looks like a StringSession (long string)
    if session_value and len(session_value) > 100:
        session = StringSession(session_value)
        client_id = phone # Use phone as stable ID for tracking
    else:
        session = session_value
        client_id = session_value

    client = TelegramClient(session, API_ID, API_HASH)
    await client.start(phone)
    
    @client.on(events.NewMessage(incoming=True))
    async def handler_new(event):
        await capture_event(client_id, event, "NEW")

    @client.on(events.MessageEdited(incoming=True))
    async def handler_edit(event):
        await capture_event(client_id, event, "EDIT")

    @client.on(events.MessageDeleted())
    async def handler_delete(event):
        for msg_id in event.deleted_ids:
            key = (client_id, msg_id)
            if key in captured_messages:
                timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                captured_messages[key].append((timestamp, "[DELETED]", "DELETE"))

    return client, client_id

def format_captured_history(history):
    if not history:
        return "*(No response)*"
    
    formatted = []
    for ts, text, ev_type in history:
        if ev_type == "NEW":
            formatted.append(f"[{ts}] {text}")
        elif ev_type == "EDIT":
            formatted.append(f"[{ts}] (EDITED): {text}")
        elif ev_type == "DELETE":
            formatted.append(f"[{ts}] (DELETED)")
    
    return "<br>".join(formatted).replace("\n", "<br>")

async def main():
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT_FILE.exists():
        print(f"Error: {INPUT_FILE} not found.")
        return

    with INPUT_FILE.open("r") as f:
        inputs = [line.strip() for line in f if line.strip()]

    print(f"Starting Blue Team Test with {len(inputs)} inputs...")
    
    print(f"Connecting Owner ({OWNER_PHONE})...")
    owner_client, owner_id = await setup_client(OWNER_SESSION, OWNER_PHONE)
    
    print(f"Connecting Collaborator ({COLLABORATOR_PHONE})...")
    collaborator_client, collaborator_id = await setup_client(COLLABORATOR_SESSION, COLLABORATOR_PHONE)

    report_header = f"# Blue Team Test Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report_header += f"| Input Prompt | Owner ({OWNER_PHONE}) Response | Collaborator ({COLLABORATOR_PHONE}) Response |\n"
    report_header += f"| :--- | :--- | :--- |\n"

    with REPORT_FILE.open("w") as rf:
        rf.write(report_header)

    for i, prompt in enumerate(inputs):
        print(f"[{i+1}/{len(inputs)}] Testing: {prompt}")

        async def run_prompt(client, client_id, client_name):
            print(f"  Sending from {client_name}...")
            # Get latest message ID to know where to start capturing
            messages = await client.get_messages(BOT_USERNAME, limit=1)
            start_id = messages[0].id if messages else 0
            
            await client.send_message(BOT_USERNAME, prompt)
            
            resp_history = []
            for _ in range(MAX_RESPONSE_WAIT_SECONDS):
                resp_history = []
                for (c_id, m_id), history in captured_messages.items():
                    if c_id == client_id and m_id > start_id:
                        resp_history.extend(history)

                if resp_history:
                    break

                await asyncio.sleep(1)

            # Sort by timestamp
            resp_history.sort(key=lambda x: x[0])
            return format_captured_history(resp_history)

        owner_resp = await run_prompt(owner_client, owner_id, "Owner")
        print("  Waiting 5 seconds before next request to avoid spamming...")
        await asyncio.sleep(5)

        collaborator_resp = await run_prompt(collaborator_client, collaborator_id, "Collaborator")

        with REPORT_FILE.open("a") as rf:
            p_escaped = prompt.replace("|", "\\|").replace("\n", " ")
            o_escaped = owner_resp.replace("|", "\\|")
            c_escaped = collaborator_resp.replace("|", "\\|")
            rf.write(f"| {p_escaped} | {o_escaped} | {c_escaped} |\n")

        print("  Waiting 5 seconds before next round to avoid spamming...")
        await asyncio.sleep(5)

    print(f"Test complete. Report saved to {REPORT_FILE}")
    await owner_client.disconnect()
    await collaborator_client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())

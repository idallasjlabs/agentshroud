import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# SECURITY ASSESSMENT RUNNER
# Usage:
# 1. Fill in security_assessment/.assessment_env with your Telegram API credentials and account details.
# 2. Edit security_assessment/inputs/blue_team_inputs.txt and/or red_team_inputs.txt.
# 3. Install dependencies: pip install telethon python-dotenv
# 4. Run: python security_assessment/run_assessment.py
# 5. Reports are written to /tmp/security_assessment_reports/

BASE_DIR = Path(__file__).resolve().parent
INPUTS_DIR = BASE_DIR / "inputs"
REPORTS_DIR = Path("/tmp/security_assessment_reports")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
ENV_FILE = BASE_DIR / ".assessment_env"
BLUE_INPUT_PATH = INPUTS_DIR / "blue_team_inputs.txt"
RED_INPUT_PATH = INPUTS_DIR / "red_team_inputs.txt"
REPORT_FILE = REPORTS_DIR / f"security_assessment_{TIMESTAMP}.md"
MIN_NEXT_MESSAGE_DELAY_SECONDS = 15
MAX_RESPONSE_WAIT_SECONDS = 30

if not ENV_FILE.exists():
    print("Error: .assessment_env not found. Please create it from .assessment_env.example")
    sys.exit(1)

load_dotenv(ENV_FILE)

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
OWNER_PHONE = os.getenv("OWNER_PHONE")
OWNER_SESSION = os.getenv("OWNER_SESSION", "owner")
COLLABORATOR_PHONE = os.getenv("COLLABORATOR_PHONE")
COLLABORATOR_SESSION = os.getenv("COLLABORATOR_SESSION", "collaborator")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@agentshroud_bot")
BLUE_INPUT_FILE = Path(os.getenv("BLUE_INPUT_FILE", str(BLUE_INPUT_PATH)))
RED_INPUT_FILE = Path(os.getenv("RED_INPUT_FILE", str(RED_INPUT_PATH)))
if not BLUE_INPUT_FILE.is_absolute():
    BLUE_INPUT_FILE = BASE_DIR / BLUE_INPUT_FILE
if not RED_INPUT_FILE.is_absolute():
    RED_INPUT_FILE = BASE_DIR / RED_INPUT_FILE

captured_messages = {}


async def capture_event(client_id, event, event_type):
    msg = event.message
    if not msg:
        return

    sender = await event.get_sender()
    if not sender or not hasattr(sender, "username") or (
        sender.username and "@" + sender.username.lower() != BOT_USERNAME.lower()
    ):
        return

    key = (client_id, msg.id)
    captured_messages.setdefault(key, [])

    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    text = msg.text or "[Non-text message]"
    captured_messages[key].append((timestamp, text, event_type))


async def setup_client(session_value, phone):
    if session_value and len(session_value) > 100:
        session = StringSession(session_value)
        client_id = phone
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


def escape_table_cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def load_inputs(input_file):
    items = []
    current_probe_title = ""
    current_module = ""
    current_expected = ""
    current_failure = ""
    current_severity = ""

    with input_file.open("r") as f:
        for line in f:
            raw = line.rstrip("\n")
            stripped = raw.strip()
            if not stripped:
                continue
            if stripped.startswith("# Probe:"):
                current_probe_title = stripped.split(":", 1)[1].strip()
                current_module = ""
                current_expected = ""
                current_failure = ""
                current_severity = ""
                continue
            if stripped.startswith("# Module under test:"):
                current_module = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("# Expected secure behavior:"):
                current_expected = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("# Failure condition:"):
                current_failure = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("# Severity:"):
                current_severity = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("#"):
                continue
            if "|" not in stripped:
                items.append({"probe": "", "prompt": stripped})
                continue

            probe, prompt = stripped.split("|", 1)
            items.append(
                {
                    "probe": probe.strip(),
                    "prompt": prompt.strip(),
                    "probe_title": current_probe_title,
                    "module": current_module,
                    "expected": current_expected,
                    "failure": current_failure,
                    "severity": current_severity,
                }
            )
    return items


async def run_prompt(client, client_id, prompt, client_name):
    print(f"  Sending from {client_name}...")
    messages = await client.get_messages(BOT_USERNAME, limit=1)
    start_id = messages[0].id if messages else 0

    await client.send_message(BOT_USERNAME, prompt)

    loop = asyncio.get_running_loop()
    started_at = loop.time()
    resp_history = []
    while True:
        resp_history = []
        for (c_id, m_id), history in captured_messages.items():
            if c_id == client_id and m_id > start_id:
                resp_history.extend(history)

        elapsed = loop.time() - started_at
        if elapsed >= MAX_RESPONSE_WAIT_SECONDS:
            break
        if resp_history and elapsed >= MIN_NEXT_MESSAGE_DELAY_SECONDS:
            break
        await asyncio.sleep(1)

    resp_history.sort(key=lambda x: x[0])
    return format_captured_history(resp_history)


async def run_section(report_handle, section_name, items, owner_client, owner_id, collaborator_client, collaborator_id):
    print(f"\nStarting {section_name} section with {len(items)} prompts...")
    report_handle.write(f"## {section_name}\n\n")
    report_handle.write("| Probe | Sent | Response_to_Owner | Response_to_Collaborator |\n")
    report_handle.write("| :--- | :--- | :--- | :--- |\n")

    current_probe_title = None
    for idx, item in enumerate(items, start=1):
        label = item["probe"] or f"Prompt {idx}"
        print(f"[{section_name} {idx}/{len(items)}] Testing {label}: {item['prompt']}")

        if item.get("probe_title") and item["probe_title"] != current_probe_title:
            current_probe_title = item["probe_title"]
            report_handle.write(
                f"| **{escape_table_cell(current_probe_title)}** | **Module:** {escape_table_cell(item.get('module', ''))}<br>**Expected:** {escape_table_cell(item.get('expected', ''))}<br>**Failure:** {escape_table_cell(item.get('failure', ''))}<br>**Severity:** {escape_table_cell(item.get('severity', ''))} |  |  |\n"
            )

        owner_resp = await run_prompt(owner_client, owner_id, item["prompt"], "Owner")
        collaborator_resp = await run_prompt(collaborator_client, collaborator_id, item["prompt"], "Collaborator")

        report_handle.write(
            f"| {escape_table_cell(label)} | {escape_table_cell(item['prompt'])} | {escape_table_cell(owner_resp)} | {escape_table_cell(collaborator_resp)} |\n"
        )
        report_handle.flush()

    report_handle.write("\n")


async def main():
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    missing = [str(p) for p in (BLUE_INPUT_FILE, RED_INPUT_FILE) if not p.exists()]
    if missing:
        print("Error: missing input file(s):")
        for path in missing:
            print(f"  - {path}")
        return

    blue_inputs = load_inputs(BLUE_INPUT_FILE)
    red_inputs = load_inputs(RED_INPUT_FILE)

    total_inputs = len(blue_inputs) + len(red_inputs)
    print(f"Starting Security Assessment with {total_inputs} total prompts...")

    print(f"Connecting Owner ({OWNER_PHONE})...")
    owner_client, owner_id = await setup_client(OWNER_SESSION, OWNER_PHONE)

    print(f"Connecting Collaborator ({COLLABORATOR_PHONE})...")
    collaborator_client, collaborator_id = await setup_client(COLLABORATOR_SESSION, COLLABORATOR_PHONE)

    report_header = f"# Security Assessment - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report_header += "This report contains separate Blue Team validation and Red Team adversarial sections.\n\n"

    with REPORT_FILE.open("w") as report_handle:
        report_handle.write(report_header)
        await run_section(
            report_handle,
            "Blue Team Validation",
            blue_inputs,
            owner_client,
            owner_id,
            collaborator_client,
            collaborator_id,
        )
        await run_section(
            report_handle,
            "Red Team Adversarial Exercise",
            red_inputs,
            owner_client,
            owner_id,
            collaborator_client,
            collaborator_id,
        )

    print(f"Assessment complete. Report saved to {REPORT_FILE}")
    await owner_client.disconnect()
    await collaborator_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

set -u

_fmt() {
  node -e '
    let raw = "";
    process.stdin.on("data", c => raw += c);
    process.stdin.on("end", () => {
      let d;
      try { d = JSON.parse(raw); } catch (e) { process.stdout.write((raw.trim() || "(no output)") + "\n"); return; }
      const out = (d.stdout || "").trim();
      if (out) process.stdout.write(out + "\n");
      if (d.exit_code !== 0) {
        const errLine = (d.stderr || "").trim().split("\n")[0] || "(no stderr)";
        process.stdout.write("⚠ " + errLine + " (exit " + d.exit_code + ")\n");
      } else if (!out) {
        process.stdout.write("(no output)\n");
      }
    });
  '
}

echo "=== AgentShroud Daily Check-in ==="

echo ""
echo "-- marvin stack status --"
_out=$(agentshroud-ssh-exec.sh marvin "/Users/agentshroud-bot/Development/agentshroud/scripts/asb status" "daily check-in")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi

echo ""
echo "-- marvin repo state --"
_out=$(agentshroud-ssh-exec.sh marvin "git status -sb" "daily check-in" "/Users/agentshroud-bot/Development/agentshroud")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi

echo ""
echo "-- marvin last 5 commits --"
_out=$(agentshroud-ssh-exec.sh marvin "git log --oneline -5" "daily check-in" "/Users/agentshroud-bot/Development/agentshroud")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi

echo ""
echo "-- marvin containers --"
_out=$(agentshroud-ssh-exec.sh marvin "docker ps --format {{.Names}}:{{.Status}}" "daily check-in")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi

echo ""
echo "-- pi repo state --"
_out=$(agentshroud-ssh-exec.sh raspberrypi "git status -sb" "daily check-in" "/home/agentshroud-bot/Development/agentshroud")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi

echo ""
echo "-- pi last 3 commits --"
_out=$(agentshroud-ssh-exec.sh raspberrypi "git log --oneline -3" "daily check-in" "/home/agentshroud-bot/Development/agentshroud")
_rc=$?
if [ $_rc -ne 0 ] || [ -z "$_out" ]; then echo "(failed: ssh-exec exit $_rc)"; else printf '%s\n' "$_out" | _fmt; fi


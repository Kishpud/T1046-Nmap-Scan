from collections import Counter
import re

log_path = "auth.log"  # Change this to your exported journal file if needed

try:
    with open(log_path, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Log file not found. Make sure auth.log exists or export journalctl logs to a file.")
    exit(1)

ip_list = []

# Match IPv4 address pattern
ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")

for line in lines:
    if "Failed password" in line:
        match = ip_pattern.search(line)
        if match:
            ip_list.append(match.group())

# Count occurrences
ip_counts = Counter(ip_list)

# Filter IPs with more than 5 failed attempts
blocklist = [ip for ip, count in ip_counts.items() if count > 5]

# Save to file
with open("blocklist.txt", "w") as f:
    for ip in blocklist:
        f.write(ip + "\n")

print("✅ Blocklist saved to blocklist.txt")
print("Offending IPs:", blocklist)

import subprocess
import re
from collections import Counter

threshold = 5  # Ban if more than 5 failures

command = "journalctl -u ssh -n 1000 | grep 'Failed password'"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

failed_logs = result.stdout
ips = re.findall(r'from (\d+\.\d+\.\d+\.\d+)', failed_logs)
ip_counts = Counter(ips)

print("🔍 SSH Brute-force Attempts (Top IPs):\n")
for ip, count in ip_counts.most_common():
    print(f"{ip} => {count} failed attempts")
    
    # Block attacker IP if it exceeds threshold
    if count > threshold:
        block_command = f"sudo ufw deny from {ip}"
        subprocess.run(block_command, shell=True)
        print(f"🚫 IP {ip} has been blocked via UFW.")

if not ip_counts:
    print("No failed SSH login attempts detected.")


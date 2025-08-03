# 🛡️ MITRE ATT&CK T1046 – Network Scanning Detection Lab

This project simulates and detects adversary behavior using `nmap` for stealthy network scanning. Detection is performed using `Zeek`, and logs are ingested and visualized with `Filebeat` and the Elastic Stack.

---

## 🎯 Objective

To emulate a real-world **MITRE ATT&CK Technique T1046** – *Network Service Scanning* – and detect the activity using Zeek logs and visual analysis in Kibana.

---

## 🔧 Tools Used

| Tool         | Purpose                              |
|--------------|--------------------------------------|
| **Nmap**     | Stealth SYN scan simulation          |
| **Zeek**     | Capture connection logs              |
| **Filebeat** | Ship logs to Elastic Cloud           |
| **Kibana**   | Visualize attacker behavior          |
| **Elastic Cloud** | Hosted SIEM + log analytics     |

---

## ⚙️ Attack Simulation

```bash
sudo nmap -sS -T4 192.168.64.0/24
Simulates stealth network discovery (TCP SYN scan)

Zeek logs the connections in conn.log

Filebeat forwards logs to Elastic Cloud

🔍 Detection Artifacts
Zeek conn.log showed multiple connections with state S0 (SYN sent, no response)

Single source IP scanned multiple ports/hosts

Kibana dashboard created to visualize scanning behavior

📊 Kibana Visualization
📁 File: screenshots/donut_dashboard.png

This donut chart visualizes Top Source IPs by connection volume. The attacker (192.168.64.28) was responsible for over 50% of the connection attempts, consistent with active scanning behavior.

📂 Files in This Project
File	Description
nmap_scan_output.txt	Raw output from the simulated scan
zeek_conn_log_sample.log	Sample from Zeek conn.log during attack
s0_only.log	Filtered connections with S0 state
screenshots/donut_dashboard.png	Kibana chart of top source IPs

📌 MITRE ATT&CK Technique Reference
Tactic	Technique Name	Technique ID
Reconnaissance	Network Service Scanning	T1046

🧠 Key Learnings
Simulated real adversary behavior in a safe lab

Detected and analyzed connection patterns using Zeek

Built meaningful visualizations to support triage

Documented detection pipeline similar to real SOCs

🗂️ Project Status
✅ Simulation completed
✅ Zeek logs captured and parsed
✅ Dashboard created
✅ Project pushed to GitHub
🔜 Upcoming: MITRE T1110 (Brute-force Attack) detection

🙌 Let's Connect
I’m actively building a hands-on SOC Analyst portfolio.
If you're hiring, mentoring, or want to collaborate — connect on LinkedIn.

yaml
Copy
Edit

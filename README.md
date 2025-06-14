

## 🛡️ ParaFinder1 — by CYBERGUARDIANS‑T

**ParaFinder1** is a minimal, fast, and dependency-free bug bounty recon tool designed for **WSL and Linux**.
It automatically discovers subdomains, extracts URLs, and flags vulnerable parameters like:

* **🔁 Open Redirect** – e.g. `?next=`, `?url=`, `?redir=`
* **📁 Local File Inclusion (LFI)** – e.g. `?file=`, `?page=`
* **🌐 Server-Side Request Forgery (SSRF)** – e.g. `?uri=`, `?domain=`

🎯 Built to eliminate boring setup steps — your users can run it **right away**.

---

### ✨ Features

* ✅ No need to install `subfinder`, `gau`, or any third-party tools
* 🧠 Built-in subdomain discovery (ping-based DNS brute)
* 📥 Basic internal crawler using `curl` to collect endpoint URLs
* 🎯 Scans for high-impact bug bounty parameters (LFI, SSRF, Redirect)
* 💻 Works on **WSL**, **Ubuntu**, **Kali**, and all Linux distros
* 🎨 Includes a banner for **CYBERGUARDIANS‑T**

---

### 🔧 Setup Instructions

#### 🧪 Works Out of the Box!

```bash
# 1. Clone the repo
git clone https://github.com/Cyb3rGu4rd14n5-T/parafinder1.git
cd parafinder1

# 2. Run the tool
python3 bughunter-tool.py -u example.com -o results.txt
```

📁 `results.txt` will contain all flagged vulnerable URLs like:

```
OPENREDIRECT suspected: http://sub.example.com/page?next=https://evil.com
LFI suspected: http://dev.example.com/view?file=../../etc/passwd
```

---

### 💡 Example Usage

```bash
python3 bughunter-tool.py -u nasa.gov
```

```bash
python3 bughunter-tool.py -u nasa.gov -o nasa-findings.txt
```

---

### 📂 Output

* ✅ Printed results: Vulnerable parameter URLs
* ✅ Saved results: If `-o` is used, stores into `.txt` file
* ✅ Optional: Customize wordlist and parameters inside the code

---

### 🧠 Author

Tool by **CYBERGUARDIANS‑T** 🛡️
Designed to simplify recon for new and elite hunters alike.



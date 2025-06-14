#!/usr/bin/env python3
import os
import subprocess
from time import sleep

BANNER = r"""
         ⚔️ CYBERGUARDIANS-T TOOL ⚔️
   _______       _               _              
  |__   __|     | |             | |             
     | | ___ ___| |__   ___  ___| |_ ___  _ __  
     | |/ _ \ '__| '_ \ / _ \/ __| __/ _ \| '__| 
     | |  __/ |  | | | |  __/\__ \ || (_) | |    
     |_|\___|_|  |_| |_|\___||___/\__\___/|_|    

   ⛱️ Trident of Discovery and Impact by CYBERGUARDIANS-T ⛱️
"""

PARAMS = {
    "openredirect": ["?next=", "?url=", "?target=", "?rurl=", "?dest=", "?destination=", "?redir="],
    "lfi": ["?file=", "?path=", "?page=", "?template=", "?inc=", "?include=", "?mod=", "?folder="],
    "ssrf": ["?url=", "?uri=", "?path=", "?target=", "?dest=", "?domain=", "?load=", "?link="]
}

OUTPUT_DIR = "output"

# Setup output structure
def setup():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open("banner.txt", "w") as b:
        b.write(BANNER)
    with open("CREDITS.txt", "w") as c:
        c.write("Tool by CYBERGUARDIANS-T\nPowered by the spirit of hackers.")
    with open("HOW_TO_SETUP.txt", "w") as s:
        s.write("""
# HOW TO SETUP

### Requirements:
- Python 3
- subfinder (https://github.com/projectdiscovery/subfinder)

### Install subfinder:
1. Download and install subfinder:
   ```bash
   curl -s https://api.github.com/repos/projectdiscovery/subfinder/releases/latest \
     | grep browser_download_url \
     | grep linux_amd64.zip \
     | cut -d '"' -f 4 \
     | wget -qi -
   unzip subfinder*.zip
   sudo mv subfinder /usr/local/bin/
   chmod +x /usr/local/bin/subfinder
   ```

2. Install Python dependencies (if any):
   ```bash
   sudo apt install python3 -y
   sudo apt install unzip wget curl -y
   ```

3. Run the tool:
   ```bash
   python3 bughunter-tool.py
   ```

4. Outputs will be stored in the "output" folder.

        """)

# Run subfinder to get subdomains
def run_subfinder(domain):
    print("[+] Running subfinder...")
    output_file = os.path.join(OUTPUT_DIR, "subdomains.txt")
    subprocess.run(["subfinder", "-d", domain, "-o", output_file])
    print(f"[+] Subdomains saved to {output_file}")
    return output_file

# Filter subdomains for parameter-based URLs
def find_param_urls(subdomain_file, param_type):
    print(f"[+] Searching for {param_type.upper()} parameters...")
    out_file = os.path.join(OUTPUT_DIR, f"{param_type}para.txt")
    param_list = PARAMS.get(param_type.lower())
    if not param_list:
        print("[-] Invalid parameter type!")
        return

    with open(subdomain_file, 'r') as f:
        lines = f.read().splitlines()

    result_urls = []
    for sub in lines:
        for p in param_list:
            result_urls.append(f"https://{sub}/{p}")

    with open(out_file, "w") as f:
        for url in result_urls:
            f.write(url + "\n")

    print(f"[+] Results written to {out_file}")


def main():
    setup()
    print(BANNER)
    domain = input("Enter the domain to find subdomains: ")
    subdomain_file = run_subfinder(domain)

    print("\nChoose parameter type to find:")
    print("1. Open Redirect")
    print("2. LFI")
    print("3. SSRF")
    choice = input("Enter choice (1/2/3): ")

    param_map = {"1": "openredirect", "2": "lfi", "3": "ssrf"}
    param_type = param_map.get(choice)

    if param_type:
        find_param_urls(subdomain_file, param_type)
    else:
        print("[-] Invalid choice")

if __name__ == "__main__":
    main()

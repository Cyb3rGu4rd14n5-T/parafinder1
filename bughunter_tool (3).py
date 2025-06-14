#!/usr/bin/env python3
# ParaFinder1 by CYBERGUARDIANS-T
# All-in-one tool with built-in subfinder (no external install needed)

import os
import subprocess
import argparse
import re
from urllib.parse import urlparse, parse_qs

# ASCII Banner
print(r"""
   _____ _     _               _                      ______         _   
  / ____| |   (_)             | |                    |  ____|       | |  
 | |    | |__  _ _ __ ___  ___| |_ ___  _ __ _   _   | |__ _ __   __| |_ 
 | |    | '_ \| | '__/ _ \/ __| __/ _ \| '__| | | |  |  __| '_ \ / _` | |
 | |____| | | | | | |  __/\__ \ || (_) | |  | |_| |  | |  | | | | (_| | |
  \_____|_| |_|_|_|  \___||___/\__\___/|_|   \__, |  |_|  |_| |_|\__,_|_|
                                             __/ |                      
                                            |___/         by CYBERGUARDIANS-T
""")

# Common LFI, SSRF, Open Redirect parameters
PARAMS = {
    "lfi": ["file", "filepath", "path", "template", "page", "include"],
    "ssrf": ["url", "uri", "path", "continue", "domain", "callback", "return", "next", "data"],
    "openredirect": ["next", "url", "target", "rurl", "dest", "destination", "redir"]
}

# Built-in subfinder replacement (lightweight DNS brute)
def builtin_subfinder(domain):
    print(f"[+] Discovering subdomains for: {domain}")
    wordlist = ["www", "mail", "ftp", "api", "dev", "staging", "test", "portal", "login", "data"]
    found = []
    for sub in wordlist:
        try:
            full = f"{sub}.{domain}"
            result = subprocess.run(["ping", "-c", "1", full], stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                print(f"[+] Found: {full}")
                found.append(full)
        except:
            continue
    return found

# Dummy GAU alternative (basic curl grepping)
def dummy_url_grabber(subdomain):
    try:
        result = subprocess.check_output(["curl", "-s", f"http://{subdomain}"], stderr=subprocess.DEVNULL)
        links = re.findall(r'href=["\']?([^"\'>]+)', result.decode())
        return [f"http://{subdomain}{l}" for l in links if l.startswith("/")]
    except:
        return []

def find_vulnerable_params(urls):
    findings = []
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for key in params:
            for vuln_type, keys in PARAMS.items():
                if key.lower() in keys:
                    findings.append(f"{vuln_type.upper()} suspected: {url}")
    return findings

def save_output(data, filename):
    with open(filename, "w") as f:
        for line in data:
            f.write(line + "\n")
    print(f"[+] Output saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="ParaFinder1 by CYBERGUARDIANS-T")
    parser.add_argument("-u", "--url", help="Target domain", required=True)
    parser.add_argument("-o", "--output", help="Output file (optional)")
    args = parser.parse_args()

    subdomains = builtin_subfinder(args.url)
    all_urls = []
    for sub in subdomains:
        all_urls.extend(dummy_url_grabber(sub))

    findings = find_vulnerable_params(all_urls)
    for f in findings:
        print(f)

    if args.output:
        save_output(findings, args.output)

if __name__ == "__main__":
    main()

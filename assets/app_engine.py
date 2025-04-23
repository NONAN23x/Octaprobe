# This file is part of the Octaprobe project.
# It is subject to the license terms in the LICENSE file found 
# in the top-level directory of this distribution
# -------------------------------------------
# Supporting libraries for our custom scanner
# -------------------------------------------

import os
import subprocess
import requests

def initialize():
    """
    Utility function to win over quick and easy hacks
    """
    PAGES_DIR = "pages"
    os.makedirs(PAGES_DIR, exist_ok=True)
    return PAGES_DIR

class Scanner:
    """
    Custom Scanner Class to run security scans on the given target
    """
    def __init__(self, ip: str):
        self.ip = ip

    def run_basic_scan(self) -> str:
        cmd = ["nmap", "-T5", self.ip]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=90)
        open_ports = []
        for line in result.splitlines():
            if "/tcp" in line and "open" in line:
                try:
                    port = int(line.split("/")[0].strip())
                    open_ports.append(port)
                except ValueError:
                    continue
        return open_ports if open_ports else [0]

    def run_advanced_scan(self) -> None:
        cache_dir = os.path.join(os.getcwd(), ".cache")
        os.makedirs(cache_dir, exist_ok=True)
        output_file = os.path.join(cache_dir, f"{self.ip}_advanced.gnmap")
        cmd = ["nmap", "-T5", "-sV", "-F", "-oG", output_file, self.ip]
        subprocess.run(cmd, stderr=subprocess.STDOUT, text=True, timeout=300)
    
    def run_web_scan(self, wordlist_path: str = None) -> None:
        print("Starting web scan...")
        url_base = f"http://{self.ip}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        discovered_endpoints = [] 
        print("Engine Breakpoint 0")
        if wordlist_path is None:
            wordlist_path = os.path.join(os.path.dirname(__file__), "wordlists", "wordlist.txt")

        try:
            with open(wordlist_path, "r") as f:
                for line in f:
                    path = line.strip()
                    if not path:
                        continue
                    target = url_base + path
                    try:
                        response = requests.get(target, headers=headers, timeout=3)
                        if response.status_code == 200:
                            discovered_endpoints.append(path)
                    except requests.RequestException:
                        pass
        except FileNotFoundError:
            print(f"Wordlist file not found: {wordlist_path}")
        
        return self.ip, discovered_endpoints

        # Example usage:
        # dirbust("192.168.1.1", "wordlist.txt")

    

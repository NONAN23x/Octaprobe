# This file is part of the Octaprobe project.
# It is subject to the license terms in the LICENSE file found 
# in the top-level directory of this distribution
# -------------------------------------------
# Supporting libraries for our custom scanner
# -------------------------------------------

import os
import subprocess
import requests
import json
import socket
import concurrent.futures

def initialize():
    """
    Utility function to win over quick and easy hacks
    """
    PAGES_DIR = "pages"
    os.makedirs(PAGES_DIR, exist_ok=True)
    
    cache_file = os.path.join(os.getcwd(), "assets", "data", ".cve_cache.json")
    if not os.path.exists(cache_file):
        with open(cache_file, "w") as f:
            json.dump({"timestamp": 0, "cves": []}, f)
    
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        nmapInstalled = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        nmapInstalled = False

    return nmapInstalled, PAGES_DIR

class Scanner:
    """
    Custom Scanner Class to run security scans on the given target
    """
    def __init__(self, ip: str, ports=None, timeout=2):
        self.ip = ip
        self.ports = ports if ports else range(1, 1024)
        self.timeout = timeout
        self.results = []

    def scan_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(self.timeout)
            result = s.connect_ex((self.ip, port))
            if result == 0:
                try:
                    s.send(b'\n')
                    banner = s.recv(1024).decode(errors="ignore").strip()
                    if not banner:
                        banner = "Couldn't Identify Banner"
                    else:
                        # Sanitize banner: keep only until first \r or \n
                        banner = banner.split('\r')[0].split('\n')[0]
                except:
                    banner = "Couldn't Identify Banner"
                return {"port": port, "banner": banner}
        return None
    
    def run_scan(self, max_workers=100, save_to_file=True):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.scan_port, port): port for port in self.ports}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.results.append(result)
        self.results.sort(key=lambda x: x["port"]) # to sort the results by port number, because concurrent scan may not be in order
        if save_to_file:
            filename = os.path.join(os.getcwd(), ".cache", f"{self.ip}_basic.json")
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(json.dumps(self.results, indent=2))
        return self.ip
    
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

    

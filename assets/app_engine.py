# This file is part of the Octaprobe project.
# It is subject to the license terms in the LICENSE file found 
# in the top-level directory of this distribution
# ------------------------------------------
# Supporting libraries for our custom scanner
# ------------------------------------------


import os
import vulners
import subprocess


def initialize():
    """
    Utility function to win over quick and easy hacks
    """
    PAGES_DIR = "pages"
    os.makedirs(PAGES_DIR, exist_ok=True)
    return PAGES_DIR

class Scanner:
    """
    Custom Scanner Class to run nmap scans on a given IP address.
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

    def run_advanced_scan(self) -> str:
        cmd = ["nmap", "-T5", "-sV", self.ip]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=180)
        open_ports = []
        for line in result.splitlines():
            if "/tcp" in line and "open" in line:
                try:
                    port = int(line.split("/")[0].strip())
                    open_ports.append(port)
                except ValueError:
                    continue
        return result if open_ports else [0]
    

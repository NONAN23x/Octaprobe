import os
import vulners
import subprocess

def initialize():
    PAGES_DIR = "pages"
    os.makedirs(PAGES_DIR, exist_ok=True)
    return PAGES_DIR


def API_KEY_SETUP():
    # Set the API Key
    api_key = os.getenv('VULNERS_API_KEY')
    if not api_key:
        raise ValueError("No API key found. Please set the VULNERS_API_KEY environment variable.")
    # print(api_key) # For Debug Purposes
    return api_key

def vulners_database(apiKey=None, args=None, filePath=None):
    vulners_api = vulners.VulnersApi(apiKey)


    project_dir = os.path.join(os.getcwd(), 'runtime', args.project)
    basic_file_path = filePath

    data = None
    try:
        with open(basic_file_path, 'r') as file:
            data = file.read()
            print(f"Data retrieved from {basic_file_path}")
    except FileNotFoundError:
        print(f"File {basic_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    print(data)


    # database_search_1 = vulners_api.find_all(
    # "sometext", limit=2,  fields=["published", "title", "description", "cvelist"])

    # print(database_search_1) # For Debug Purposes

class Scanner:
    """
    Custom Scanner Class to run nmap scans on a given IP address.
    """
    def __init__(self, ip: str):
        self.ip = ip

    def run_basic_scan(self) -> str:
        cmd = ["nmap", self.ip]
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
        cmd = ["nmap", "-sV", self.ip]
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
    
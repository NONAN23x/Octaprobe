import os
import argparse
import vulners
import nmap

def initialize():
    # Create a directory called 'runtime' in the current directory with error control
    try:
        runtime_dir = os.path.join(os.getcwd(), 'runtime')
        os.makedirs(runtime_dir, exist_ok=True)
        print(f"Directory 'runtime' created at {runtime_dir}")
    except Exception as e:
        print(f"An error occurred while creating the 'runtime' directory: {e}")
    
def args_setup():
    parser = argparse.ArgumentParser(description="Octaprobe Command Line Tool")
    parser.add_argument("mode", choices=["discover", "basic", "advanced"],
                        help="Mode of operation")
    parser.add_argument("--service", type=str, help="Specific service to scan (for advanced modes)")
    parser.add_argument("--project", type=str, required=True, help="Project name for organizing scan results (mandatory)")
    parser.add_argument("--target", type=str, required=True, help="Target IP or range for scanning (mandatory)")

    return parser.parse_args()

def create_subdirectory(args, folder_name):
        try:
            runtime_dir = os.path.join(os.getcwd(), 'runtime')
            sub_dir = os.path.join(runtime_dir, folder_name)
            os.makedirs(sub_dir, exist_ok=True)
            print(f"Subdirectory '{folder_name}' created at {sub_dir}")
            target_file = os.path.join(sub_dir, args.target + '.txt')
            with open(target_file, 'w') as f:
                f.write(f"Target: {args.target}\n")
            print(f"File '{args.target}.txt' created in subdirectory '{folder_name}'")

            return sub_dir
        except Exception as e:
            print(f"An error occurred while creating the subdirectory '{folder_name}': {e}")
            return None

class Scanner:
    def __init__(self, target, project):
        self.target = target
        self.project = project

    def discover(self):
        print(f"Performing discovery scan on target: {self.target}")
        nm = nmap.PortScanner()
        try:
            nm.scan(hosts=self.target, arguments='-sn')
            sub_dir = create_subdirectory(argparse.Namespace(target=self.target, project=self.project), self.project)
            if sub_dir:
                result_file = os.path.join(sub_dir, 'discovery_results.txt')
                with open(result_file, 'w') as f:
                    for host in nm.all_hosts():
                        f.write(f'Host: {host}\tState: {nm[host].state()}\n')
                        print(f'Host: {host}\tState: {nm[host].state()}')
                print(f"Discovery results saved to {result_file}")
        except Exception as e:
            print(f"An error occurred during the discovery scan: {e}")

    def basic(self):
        print(f"Performing basic scan on target: {self.target}")
        nm = nmap.PortScanner()
        try:
            nm.scan(hosts=self.target, arguments='-sV')
            sub_dir = create_subdirectory(argparse.Namespace(target=self.target, project=self.project), self.project)
            if sub_dir:
                result_file = os.path.join(sub_dir, 'basic_scan_results.txt')
                with open(result_file, 'w') as f:
                    for host in nm.all_hosts():
                        f.write(f'Host: {host}\tState: {nm[host].state()}\n')
                        print(f'Host: {host}\tState: {nm[host].state()}')
                        for proto in nm[host].all_protocols():
                            f.write(f'Protocol: {proto}\n')
                            print(f'Protocol: {proto}')
                            lport = nm[host][proto].keys()
                            for port in lport:
                                state = nm[host][proto][port]["state"]
                                service = nm[host][proto][port].get("name", "unknown")
                                # version = nm[host][proto][port].get("version", "unknown")
                                cpe=nm[host][proto][port].get("cpe", "unknown")
                                f.write(nm.csv())
                                print(f'Port: {port}\tState: {state}\tService: {service}\tVersion: {cpe}')
                                print(nm.csv())
                print(f"Basic scan results saved to {result_file}")
        except Exception as e:
            print(f"An error occurred during the basic scan: {e}")

    def advanced(self):
        print(f"Performing advanced version probing scan on target: {self.target}")
        nm = nmap.PortScanner()
        try:
            nm.scan(hosts=self.target, arguments='-sV')
            for host in nm.all_hosts():
                print(f'Host : {host}')
            for proto in nm[host].all_protocols():
                print(f'Protocol : {proto}')
                lport = nm[host][proto].keys()
                for port in lport:
                    state = nm[host][proto][port]["state"]
                    service = nm[host][proto][port].get("name", "unknown")
                    version = nm[host][proto][port].get("version", "unknown")
                    all = nm
                    # print(f'Port: {port}\tState: {state}\tService: {service}\tVersion: {version}')
                    print(nm.csv())
        except Exception as e:
            print(f"An error occurred during the advanced scan: {e}")


    def __init__(self, target, project, service=None):
        self.target = target
        self.project = project
        self.service = service

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


def main():

    initialize()

    args = args_setup()
        
    create_subdirectory(args, args.project)

    scanner = Scanner(args.target, args.project)

    # vulners_database(API_KEY_SETUP(), args, os.path.join(os.getcwd(), 'runtime', args.project, 'basic_scan_results.txt'))

    match args.mode:
        case "discover":
            scanner.discover()
        case "basic":
            scanner.basic()
        case "advanced":
            scanner.advanced()
        case _:
            print("Invalid mode selected")




if __name__ == "__main__":
    # Your code here
    main()
###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################


import subprocess
import os
import sys
import webbrowser

OS = sys.platform
BASE_MODEL= "gemma3:1b"
MODELFILE_PATH = os.path.join(os.path.dirname(__file__), "assets", "Modelfile.txt")
MODEL_NAME = "octabot"
SYSTEM_PROMPT = """
You are OctaBot, a cybersecurity-focused assistant designed to help users with both general cybersecurity concepts and the functionality of a tool called OctaProbe.
Your primary focus is on cybersecurity topics including but not limited to:
- Vulnerability scanning and reporting
- CVSS scoring (v3.1 and v4.0)
- Network enumeration and OSINT
- Penetration testing tools and techniques
- API security and testing
- Secure coding, cryptography, and threat modeling
You also serve as the in-tool assistant for OctaProbe, a cybersecurity utility that provides the following key features:
1. Directory Fuzzing and Port Scanning
    - Uses customizable wordlists to discover hidden files and directories on a web server.
    - Supports intelligent filtering and concurrent scanning for speed.
2. Checksums Generator
    - Generates and verifies file checksums (e.g., MD5, SHA-256) to ensure file integrity.
3. Malware Analysis
    - Analyzes entropy of Windows PE (Portable Executable) or Unix ELF (Executable Linked Format) files to detect signs of packing or obfuscation.
4. OctaBot AI Assistant
    - Provides cybersecurity guidance and explanations for OctaProbe's features.
5. API Tester
    - GUI-based interface to send GET and POST requests.
    - Custom headers and payloads supported via Streamlit widgets.
    - Includes default headers and response formatting for easier debugging.
6. Cheatsheets Menu
    - Includes quick-reference guides for:
      - Linux Hardening
      - Windows Hardening
      - Black Box Enumeration
      - Web App Security
If users ask about any of these modules, explain how to use them, what input they require, and what the output means. Always be concise, helpful, and stay within the domain of cybersecurity and OctaProbe.
If a question is outside the scope of cybersecurity or OctaProbe, politely decline and steer the conversation back to relevant topics.
You are not a general-purpose AI. Always be brief about your answers as you're being deployed on local hardware. You are a professional cybersecurity aide, designed to enhance and support secure development and testing workflows.
"""

def check_virus_total():
    api_key = os.environ.get("VIRUSTOTAL_API_KEY")
    if api_key:
        print("[✔] VIRUSTOTAL_API_KEY is set.")
    else:
        print("[-] VIRUSTOTAL_API_KEY environment variable is not set.")
        print("This API key is required for using VirusTotal features in OctaProbe.")
        try:
            user_input = input("[?] Would you like to be redirected to the VirusTotal API key page? (y/n): ").strip().lower()
            if user_input.startswith('y'):
                webbrowser.open("https://www.virustotal.com/gui/my-apikeys")
            else:
                print("You can still use the application, but VirusTotal features will be unavailable.")
        except KeyboardInterrupt:
            print("\n[!] Operation interrupted by user.")

def check_ollama():
    try:
        subprocess.run(["ollama", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[✔] Ollama is installed and running.")
    except Exception:
        print("[-] Ollama is not installed. Install it from https://ollama.com or follow the guide provided in Wiki.")
        try:
            user_input = input("[?] Would you like to be taken to the download page? (y/n): ").strip().lower()
            if user_input.startswith('y'):
                if OS.startswith("win"):
                    webbrowser.open("https://ollama.com/download/windows")
                elif OS.startswith("darwin"):
                    webbrowser.open("https://ollama.com/download/macos")
                elif OS.startswith("linux"):
                    webbrowser.open("https://ollama.com/download/linux")
                else:
                    print("[-] Unsupported OS. Please visit https://ollama.com manually.")
            else:
                print("You can still use the application without Ollama, but some features may be limited.")
                print("exiting setup...")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n[!] Operation interrupted by user. Exiting setup...")
            sys.exit(1)
        sys.exit(1)

def pull_base_model(BASE_MODEL=BASE_MODEL):
    try:
        import ollama
    except ImportError:
        print("[-] Ollama Python package is not installed. Please install it using the command: pip install ollama")
        sys.exit(1)
        print(f"[*] Pulling base model...")
        ollama.pull(BASE_MODEL)
        print("[✔] Base model pulled successfully.")
    except KeyboardInterrupt:
        print("\n[!] Pulling base model interrupted by user.")
        sys.exit(1)

def build_custom_model(model_name=MODEL_NAME, base_model=BASE_MODEL, prompt=SYSTEM_PROMPT):
    try:
        import ollama
        print(f"[*] Building custom model: {model_name}...")
        ollama.create(model=model_name, system=prompt, from_=base_model)
        print("[✔] Custom model built successfully.")
    except ImportError:
        print("[-] Ollama Python package is not installed. Please install it using the command: pip install ollama")
        sys.exit(1)

if __name__ == "__main__":
    try:
        os.system('clear')
        check_virus_total()
        check_ollama()
        pull_base_model()
        build_custom_model()
        print("[✔] Setup finished. \nYou are now ready to use OctaProbe!\n")
        print("To start the app, run: 'streamlit run app.py'.\nIf your environment is protected, run: 'python -m streamlit run app.py'")
    except Exception as e:
        print(f"[!] An error occurred during setup: {e}")

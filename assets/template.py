###############################################################################
# Octaprobe Security Scanner - Network Security Analysis Suite
# Secure, Scalable, Enterprise-Grade Scanning Infrastructure (atleast we try)
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################
# Quick and dirty template generator for Streamlit
###############################################################################


def generate_basic_template(ip: str) -> str:
    return f"""import streamlit as st
import pandas as pd
import os
import json
try :
    from ollama import ChatResponse
    from ollama import chat
    ollamaNotFound = False
except ImportError:
    ollamaNotFound = True
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")

with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
#if ollamaNotFound:
#        st.error("Ollama is not installed. Please install it to use this feature.")
#        return

def chat_with_OctaBot(userInput: str):
        response: ChatResponse = chat(model='OctaBot', stream=True, 
        messages=[{{'role': 'user','content': userInput}}])
        for chunk in response:
            yield chunk['message']['content']
            
st.divider()
st.subheader("Target: {ip}")
st.write("📄 Basic Scan Result")

cache_file = os.path.join(os.getcwd(), ".cache", "{ip}_basic.json")
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        localData = json.load(file)

    if localData:
        table_data = [
            {{"Port": entry.get("port", "N/A"), "Banner": entry.get("banner", "N/A")}}
            for entry in localData
        ]
        df = pd.DataFrame(table_data)
        st.table(df)
    else:
        st.warning("Host is down or no valid data found in the cache file.")
else:
    st.error(f"No scan data found for {ip} in cache")
"""


def generate_advanced_template(ip: str) -> str:
    return f"""import streamlit as st
import pandas as pd
import os
try :
    from ollama import ChatResponse
    from ollama import chat
    ollamaNotFound = False
except ImportError:
    ollamaNotFound = True
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")

st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")

with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
#if ollamaNotFound:
#        st.error("Ollama is not installed. Please install it to use this feature.")
#        return

st.divider()
st.subheader("Target: {ip}")
st.write("📄 Advanced Scan Result")
cache_file = os.path.join(os.getcwd(), ".cache", "localhost_advanced.gnmap")
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        local_data = file.read()

    # Extract and display lines containing port information
    port_line = next((line for line in local_data.splitlines() if "Ports:" in line), None)
    if port_line and "Ports:" in port_line:
        ports = port_line.split("Ports:")[1].strip()
        table_data = [
            {{"Port Number": p[0], "Service": p[4], "Version": p[6]}}
            for p in (port.strip().split("/") for port in ports.split(","))
            if len(p) >= 7
        ]
        if table_data:
            df = pd.DataFrame(table_data)
            st.table(df)
        else:
            st.warning("No valid port information found.")
    else:
        st.warning("No port information found in the cache file.")
        st.warning("Check the IP Address, are you sure the host is running?")

else:
    st.error(f"No scan data found for localhost in cache")
    localData = []

"""

def generate_web_template(ip: str, endpoint) -> str:
    return f"""import streamlit as st
import pandas as pd
import subprocess
import requests
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")

with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
host = "{ip}"
entries = {endpoint}
st.write("📄 Web Scan Result")
data = [{{"Endpoint": f"{ip}/{{endpoint}}"}} for endpoint in enumerate(entries, start=1)]
df = pd.DataFrame(data)
st.table(df)

col1, col2 = st.columns([0.8, 0.2])
with col1:
        customfile = st.file_uploader("Scan with a custom wordlist?", type=["txt"])
with col2:
        scan_button = st.button("Start Scan", use_container_width=True)

if customfile is not None and scan_button:
        wordlist = customfile.read().decode("utf-8").splitlines()
        progress_bar = st.progress(0)
        results = []

        for idx, word in enumerate(wordlist):
            url = f"http://{{host}}/{{word}}"
            try:
                response = requests.get(url, timeout=5)
                status_code = str(response.status_code)
                if status_code == "200":
                    results.append({{"Endpoint": url}})
            except Exception as e:
                st.error(f"Error scanning {{url}}: {{e}}")
            progress_bar.progress((idx + 1) / len(wordlist))

        progress_bar.empty()
        if results:
            st.success("Scan completed. Found the following endpoints:")
            result_df = pd.DataFrame(results)
            st.table(result_df)
        else:
            st.warning("Scan completed. No endpoints found.")

"""

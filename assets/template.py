# This file is part of the Octaprobe project.
# It is subject to the license terms in the LICENSE file found
#  at the top-level directory of this project
# --------------------------------------------
# Quick and dirty template generator for Streamlit
# --------------------------------------------


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
st.set_page_config("Octaprobe", page_icon=":octopus:")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4, col5 = st.columns(5)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")

with st.sidebar:
        st.title("📁 Scan Projects")
        st.divider()
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("View the source", url="https://github.com/NONAN23x/Octaprobe")

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
st.set_page_config("Octaprobe", page_icon=":octopus:")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4, col5 = st.columns(5)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")

with st.sidebar:
        st.title("📁 Scan Projects")
        st.divider()
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("View the source", url="https://github.com/NONAN23x/Octaprobe")

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
st.set_page_config("Octaprobe", page_icon=":octopus:")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4, col5 = st.columns(5)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")

with st.sidebar:
        st.title("📁 Scan Projects")
        st.divider()
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("View the source", url="https://github.com/NONAN23x/Octaprobe")
        
entries = {endpoint}
st.write("📄 Web Scan Result")
data = [{{"Index": idx, "Endpoint": f"{ip}/{{endpoint}}"}} for idx, endpoint in enumerate(entries, start=1)]
df = pd.DataFrame(data)
st.table(df)
"""
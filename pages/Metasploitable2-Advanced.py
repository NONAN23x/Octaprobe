import streamlit as st
import pandas as pd
import os
try :
    from ollama import ChatResponse
    from ollama import chat
    ollamaNotFound = False
except ImportError:
    ollamaNotFound = True
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Version Enumeration Scan Example")


with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
#if ollamaNotFound:
#        st.error("Ollama is not installed. Please install it to use this feature.")
#        return

st.divider()
st.subheader("Target: 192.168.1.169")
cache_file = os.path.join(os.getcwd(), ".cache", "192.168.1.169_advanced.gnmap")
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        local_data = file.read()

    # Extract and display lines containing port information
    port_line = next((line for line in local_data.splitlines() if "Ports:" in line), None)
    if port_line and "Ports:" in port_line:
        ports = port_line.split("Ports:")[1].strip()
        table_data = [
            {"Port Number": p[0], "Service": p[4], "Version": p[6]}
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
    st.error(f"No scan data found for 192.168.1.169 in cache")
    localData = []


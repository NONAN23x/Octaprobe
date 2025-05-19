import streamlit as st
import pandas as pd
import subprocess
import requests
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Web Scan Example File")

with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
host = "192.168.1.139:8080"
entries = ['admin', 'backup', 'config', 'dashboard', 'data', 'db', 'dev', 'hidden', 'images', 'login', 'private', 'server-status', 'uploads']
data = [{"Endpoint": f"192.168.1.139:8080/{endpoint}"} for endpoint in enumerate(entries, start=1)]
df = pd.DataFrame(data)
st.table(df)

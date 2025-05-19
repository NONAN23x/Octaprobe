import streamlit as st
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
st.header("Basic Scan Example")

with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")
#if ollamaNotFound:
#        st.error("Ollama is not installed. Please install it to use this feature.")
#        return

def chat_with_OctaBot(userInput: str):
        response: ChatResponse = chat(model='OctaBot', stream=True, 
        messages=[{'role': 'user','content': userInput}])
        for chunk in response:
            yield chunk['message']['content']
            
st.divider()
st.subheader("Target: 192.168.1.169")
st.write("📄 Basic Scan Result")

cache_file = os.path.join(os.getcwd(), ".cache", "192.168.1.169_basic.json")
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        localData = json.load(file)

    if localData:
        table_data = [
            {"Port": entry.get("port", "N/A"), "Banner": entry.get("banner", "N/A")}
            for entry in localData
        ]
        df = pd.DataFrame(table_data)
        st.table(df)
    else:
        st.warning("Host is down or no valid data found in the cache file.")
else:
    st.error(f"No scan data found for 192.168.1.169 in cache")

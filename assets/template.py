
def generate_basic_template(ip: str, scan_result) -> str:
    return f"""import streamlit as st
import pandas as pd
import ast
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4 = st.columns(4)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("Streamlit", color="red")
st.sidebar.title("📁 Scan Projects")

st.write("### 📄 Basic Scan Result")
st.divider()
localData = {scan_result}
st.subheader("Target: {ip}")

df = pd.DataFrame(localData, columns=["Open Ports"])
st.table(df)
"""


def generate_advanced_template(ip: str, scan_result: str) -> str:
    return f"""import streamlit as st
import pandas as pd
import ast
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4 = st.columns(4)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("Streamlit", color="red")
st.sidebar.title("📁 Scan Projects")

st.write("### 📄 Basic Scan Result")
st.divider()
localData = {scan_result}
st.subheader("Target: {ip}")

df = pd.DataFrame(localData, columns=["Open Ports"])
st.table(df)
"""
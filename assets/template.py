# This file is part of the Octaprobe project.
# It is subject to the license terms in the LICENSE file found
#  at the top-level directory of this project
# --------------------------------------------
# Quick and dirty template generator for Streamlit
# Because we are lazy
# --------------------------------------------


def generate_basic_template(ip: str, scan_result) -> str:
    return f"""import streamlit as st
import pandas as pd
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4, col5 = st.columns(5)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")
st.sidebar.title("📁 Scan Projects")

st.divider()
st.write("📄 Basic Scan Result")
localData = {scan_result}
st.subheader("Target: {ip}")

df = pd.DataFrame(localData, columns=["Open Ports"])
st.table(df)
"""


def generate_advanced_template(ip: str, scan_result) -> str:
    return f"""import streamlit as st
import pandas as pd
st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
st.title("Octaprobe")
st.header("Yet Another Vulnerability Scanner")
col1, col2, col3, col4, col5 = st.columns(5)
col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")
st.sidebar.title("📁 Scan Projects")

st.divider()
st.write("📄 Basic Scan Result")
localData = {scan_result}
st.subheader("Target: {ip}")

df = pd.DataFrame(localData, columns=["Open Ports"])
st.table(df)
"""
###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
import modules.dashboard as app
import modules.settings as settings
import modules.assistant as assistant
import modules.checksums as checksums
import modules.analysis as analysis
import modules.repeater as apiRepeater
import modules.cheatsheets as cheatsheet


def main():

    st.set_page_config("Octaprobe", page_icon=":octopus:", layout="wide")
    
    # Display the title, description and badges
    st.title("Octaprobe")
    st.header("Yet Another Security Assessment Tool")
    
    # Displaying sidebar with information
    with st.sidebar:
        st.title("📁 Scan History")
        st.write("Octaprobe is a security assessment tool designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
        st.link_button("Visit GitHub Page", url="https://github.com/NONAN23x/Octaprobe")

    # Displaying various tabs for different functionalities
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        ["**:house: Dashboard**", 
         "**:key: Checksums**",
         "**:microscope: Malware Analysis**",
         "**:link: APIs**",
         "**:notebook: Cheatsheets**",
         "**:bust_in_silhouette: Assistant**",
         "**:gear: Settings**",
         ]
        )

    with tab1:
        # Display the scan form
        with st.container(border=True):
            app.dashboard()

    with tab2:
        # Checksums tab content
        with st.container(border=True):
            checksums.generate_checksums()

    with tab3:
        # Malware Analysis tab content
        with st.container(border=True):
            analysis.analysis()
        # VirusTotal Analysis
        with st.expander("VirusTotal Analysis"):
            analysis.virus_analysis()

    with tab4:
        # API tab content
        with st.container(border=True):
            apiRepeater.repeater()

    with tab5:
        # Cheatsheets tab content
        with st.container(border=True):
            cheatsheet.sheets()

    with tab6:
        # Assistant tab content
        with st.container(border=True):
            assistant.assistant()

    with tab7:
        # Settings tab content
        with st.container(border=True):
            settings.settings()

if __name__ == "__main__":
    # Initialize the app and run the main function
    main()

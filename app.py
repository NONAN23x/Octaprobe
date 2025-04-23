import streamlit as st
import modules.dashboard as app
import modules.settings as settings
import modules.assistant as assistant
import modules.checksums as checksums
import modules.analysis as analysis
import modules.about as about

def main():

    st.set_page_config("Octaprobe", page_icon=":octopus:")
    
    # Display the title, description and badges
    st.title("Octaprobe")
    st.header("Yet Another Vulnerability Scanner")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("nmap", color='violet') ; col5.badge("Streamlit", color="red")
    st.sidebar.title("📁 Scan Projects")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["**:desktop_computer: Dashboard**", 
         "**:hash: Checksums**",
         "**:mag: Malware Analysis**",
         "**:robot_face: Assistant**",
         "**:wrench: Settings**",
         "**:information_source: About**"
         ]
        )

    with tab1:
        # Display the scan form
        app.dashboard()

    with tab2:
        # Checksums tab content
        checksums.generate_checksums()

    with tab3:
        # Malware Analysis tab content
        analysis.analysis()

    with tab4:
        # Assistant tab content
        assistant.assistant()

    with tab5:
        # Settings tab content
        settings.settings()

    with tab6:
        # About section
        about.about()




if __name__ == "__main__":
    # Initialize the app and run the main function
    # Your code here
    main()


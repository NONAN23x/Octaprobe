import assets.app_engine as engine
import streamlit as st
import re
import os
from assets.template import generate_basic_template
from assets.template import generate_advanced_template
from assets.app_engine import Scanner

def main():
    # Set the page configuration, and other workarounds
    PAGES_DIR = engine.initialize()


    # Display the title, description and badges
    st.title("Octaprobe")
    st.header("Yet Another Vulnerability Scanner")
    col1, col2, col3, col4 = st.columns(4)
    col1.badge("Python", color="violet"); col2.badge('VulnersAPI', color="orange"); col3.badge('LangChain', color='green'); col4.badge("Streamlit", color="red")
    st.sidebar.title("📁 Scan Projects")
    

    # Display the scan form
    with st.form("scan_form", clear_on_submit=False):
        ip = st.text_input("Enter Target IP Address", placeholder="e.g., 192.168.1.1")
        scan_mode = st.radio(
            "Select Scan Mode",
         options=["Basic", "Advanced"],
         index=0,
         horizontal=True)         
        submit = st.form_submit_button("🚀 Start Scan")
        
    # User input Sanitization
    def is_valid_ip_or_domain(value):
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        domain_pattern = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
        return ip_pattern.match(value) or domain_pattern.match(value)

    # Check if the form is submitted
    if submit:
        if not ip or not is_valid_ip_or_domain(ip):
            st.warning("Please enter a valid IP address or domain name.")
        else:
            st.success(f"Scan initiated for `{ip}` using **{scan_mode}** mode.")
            

            # Placeholder: You can now call your scan function here
            with st.spinner("Initializing scan..."):
                try:
                    scanner = Scanner(ip)

                    if scan_mode == "Basic":
                        result = scanner.run_basic_scan()
                        page_code = generate_basic_template(ip, result)
                    elif scan_mode == "Advanced":
                        result = scanner.run_advanced_scan()
                        page_code = generate_advanced_template(ip, result)

                    existing_files = [f for f in os.listdir(PAGES_DIR) if f.startswith("scan_") and f.endswith(".py")]
                    index = 1
                    while any(f.startswith(f"{index}_scan_") for f in existing_files):
                        index += 1
                    page_filename = f"{index}_scan_{ip.replace('.', '_')}.py"
                    with open(os.path.join(PAGES_DIR, page_filename), "w") as f:
                        f.write(page_code)

                    st.success("Scan complete. Restart app to view new page.")
                except Exception as e:
                    st.error(f"Scan failed: {e}")


if __name__ == "__main__":
    # Your code here
    main()
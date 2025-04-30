import streamlit as st
import re
import os
import time
import assets.app_engine as engine
from assets.app_engine import Scanner
from assets.template import generate_basic_template, generate_advanced_template, generate_web_template
from assets.queryCVEs import fetch_cves
import json
from datetime import datetime
from modules.settings import settings


def dashboard():
    # Set the page configuration, and other workarounds
    nmapFound, PAGES_DIR = engine.initialize()

    # Sanitize user input
    # Ensure the IP address is valid and not empty
    def is_valid_ip_or_domain(value):
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?::[0-9]{1,5})?$")
        domain_pattern = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?::[0-9]{1,5})?$")
        localhost_pattern = re.compile(r"^localhost(?::[0-9]{1,5})?$")
        return ip_pattern.match(value) or domain_pattern.match(value) or localhost_pattern.match(value)

    # Validate project name
    def is_valid_project_name(name):
        invalid_chars_pattern = re.compile(r"[^\w\- ]")  # Allow only alphanumeric, underscores, hyphens, and spaces
        return not invalid_chars_pattern.search(name)

    with st.form("scan_form", clear_on_submit=False):
        ip = st.text_input("Enter Target IP Address", placeholder="e.g., 192.168.1.1")
        
        scan_mode = st.radio("Select Scan Mode", options=["Basic", "Advanced", "Web"], index=0, horizontal=True) 

        col1, col2 = st.columns([3, 1], vertical_alignment="bottom")  # 75% for col1, 25% for col2
        with col1:
            project_name = st.text_input(
            "Enter Project Name", 
            placeholder="e.g., My Network Scan"
            )
        with col2:
            submit = st.form_submit_button(
            "🚀 Start Scan"
            )

        # main logic of the app
        # Check if the form is submitted and process the input
        if submit:
            if not ip or not is_valid_ip_or_domain(ip):
                st.warning("Please enter a valid IP address or domain name.")
                
            elif not project_name or not is_valid_project_name(project_name):
                st.warning("Please enter a valid project name.")
                st.toast("Hey, no fuzz testing this app!!!", icon="🚫")
            
            else:
                st.success(f"Scan initiated for `{ip}` using **{scan_mode}** mode.")

                # Internal App Logic: You can now call your scan function here
                with st.spinner("Initializing scan..."):
                    try:
                        scanner = Scanner(ip) # OOPs !!!    
                        if scan_mode == "Basic":
                            st.toast("Please wait 3-5 minutes for the scan to complete", icon="🔍")
                            result = scanner.run_scan()
                            page_code = generate_basic_template(result)
                        elif scan_mode == "Advanced":
                            if nmapFound:
                                st.toast("Please wait 3-5 minutes for the scan to complete", icon="🔍")
                                scanner.run_advanced_scan()
                                page_code = generate_advanced_template(ip)
                            else:
                                st.warning("Nmap not found. Please install Nmap to use this feature.")
                                st.toast("Installl all dependencies prior running this app!!!", icon="🚫")
                                return

                        elif scan_mode == "Web":
                            st.toast("Please wait 3-5 minutes for the scan to complete", icon="🔍")
                            host,endpoints = scanner.run_web_scan()
                            page_code = generate_web_template(host,endpoints)
                                                   
          
                        # Save the generated page code to a new file in the PAGES_DIR
                        sanitized_project_name = re.sub(r"[^a-zA-Z0-9_\-]", "_", project_name.strip())
                        page_filename = f"{sanitized_project_name}.py"

                        with open(os.path.join(PAGES_DIR, page_filename), "w") as f:
                            f.write(page_code)  
                        # Display a success message
                        st.toast(f"{scan_mode} Scan completed successfully!", icon="✅")
                        st.success("Scan complete. Restarting app to view the new page.")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Scan failed: {e}")

    
    # present basic recent CVE's information
    st.divider()
    data = fetch_cves()

    st.subheader("Recent CVEs")
    
    col1, col2 = st.columns([3, 1])  # 75% for col1, 25% for col2
    with col1:
        st.write("Read more about the latest CVEs on [CVE Details](https://www.cvedetails.com/)")
    with col2:
        # Load the timestamp from the .cve_cache.json file
        cve_cache_file = os.path.join("assets", "data", ".cve_cache.json")
        try:
            with open(cve_cache_file, "r") as f:
                cve_cache_data = json.load(f)
            timestamp = cve_cache_data.get("timestamp", None)
            if timestamp:
                # Convert the timestamp to a human-readable format
                last_updated_time = datetime.fromtimestamp(timestamp).strftime("%I:%M %p")
                st.badge(f"Last Updated: {last_updated_time}", color="grey")
            else:
                st.caption("Last Updated: Unknown")
        except Exception as e:
            st.caption(f"Last Updated: Error loading timestamp ({e})")
    
    if data:
        for i in range(0, len(data), 2):
            col1, col2 = st.columns(2, border=True)  # Create two columns for each row
            with col1:
                if i < len(data):
                    item = data[i]
                    cve_id = item.get("id", "N/A")
                    st.badge(cve_id, color="red")
                    st.write(f"**Summary:** {item.get('summary', 'N/A')}")
                    st.write(f"**Published Date:** {item.get('published', 'N/A')}")
                    cve_link = f"https://www.cve.org/CVERecord?id={cve_id}"
                    st.link_button("View Details", url=cve_link)

            with col2:
                if i + 1 < len(data):
                    item = data[i + 1]
                    cve_id = item.get("id", "N/A")
                    st.badge(cve_id, color="red")
                    st.write(f"**Summary:** {item.get('summary', 'N/A')}")
                    st.write(f"**Published Date:** {item.get('published', 'N/A')}")
                    cve_link = f"https://www.cve.org/CVERecord?id={cve_id}"
                    st.link_button("View Details", url=cve_link)

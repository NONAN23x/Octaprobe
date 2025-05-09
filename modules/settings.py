###############################################################################
# Octaprobe Security Scanner - Network Security Analysis Suite
# Secure, Scalable, Enterprise-Grade Scanning Infrastructure (atleast we try)
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
import os
import time


def settings():
    
    # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])

    with col1:
        st.write("#### Tune the settings to enhance your scanning experience.")
    
    with col2:
        with st.popover("💡"):
            st.write("You can customize the settings to enhance your scanning experience.")
            st.write("This includes selecting themes, managing previous scans, and configuring other preferences.")
            
    # Directory containing the pages
    pages_dir = os.path.join(os.getcwd(), "pages")

    # List all files in the pages directory
    if os.path.exists(pages_dir):
        pages = [f for f in os.listdir(pages_dir) if os.path.isfile(os.path.join(pages_dir, f))]
    else:
        pages = []

    success_message = None
    st.divider()
    if pages:
        st.badge("📁 Previous Scans")
    else:
        st.caption("💡 No previous scans were found.")

    for page in pages:
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.write(os.path.splitext(page)[0])
        with col2:
            if st.button("🗑️", key=f"delete_{page}"):
                os.remove(os.path.join(pages_dir, page))
                success_message = f"Deleted {page}"
                st.toast(f"Deleted {page}", icon="🟢")
                time.sleep(0.5)
                st.rerun()

    if success_message:
        st.success(success_message)

    st.divider()
    themeDirectory = os.path.join(os.getcwd(), "assets", "themes")
    themeData = {"Light": f"{themeDirectory}/Light.toml", 
                 "Red": f"{themeDirectory}/Red.toml", 
                 "Green": f"{themeDirectory}/Green.toml", 
                 "Blue": f"{themeDirectory}/Blue.toml", 
                 "Dark": f"{themeDirectory}/Dark.toml"}
    col1, col2, col3 = st.columns([1, 2.5, 0.5])
    with col1:
        st.write("Select theme")
    with col2:
        theme = st.radio("Theme", options=list(themeData.keys()), horizontal=True, label_visibility="collapsed")
    with col3:
        if st.button("Apply"):
            selected_theme_file = themeData.get(theme)
            if selected_theme_file and os.path.exists(selected_theme_file):
                current_dir = os.getcwd()
                streamlit_config_path = os.path.join(current_dir, ".streamlit", "config.toml")
                os.makedirs(os.path.dirname(streamlit_config_path), exist_ok=True)
                with open(selected_theme_file, "r") as theme_file:
                    theme_contents = theme_file.read()
                with open(streamlit_config_path, "w") as config_file:
                    config_file.write(theme_contents)
                st.toast(f"Theme '{theme}' applied!", icon="🟢")
                time.sleep(0.3)
                st.rerun()
            else:
                st.error(f"Theme file for '{theme}' not found!")

            st.success(f"Theme applied!")

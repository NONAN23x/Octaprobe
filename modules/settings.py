import streamlit as st
import os
import time

def settings():
    st.subheader("Settings")
    st.write("Configure your scan settings here.")

    st.divider()
    # File input for wordlist
    wordlist = None
    st.badge("⚙️ Optional")
    st.write("You can upload a custom wordlist to use for the web scan. If you don't upload one, the default wordlist will be used.")
    st.write("The default wordlist is located in the `assets/data/wordlist.txt` directory.")
    uploaded_file = st.file_uploader("Upload a custom wordlist", type="txt", accept_multiple_files=False)
        

    # Directory containing the pages
    pages_dir = os.path.join(os.getcwd(), "pages")

    # List all files in the pages directory
    if os.path.exists(pages_dir):
        pages = [f for f in os.listdir(pages_dir) if os.path.isfile(os.path.join(pages_dir, f))]
    else:
        pages = []

    st.divider()
    success_message = None

    if pages:
        st.caption("📁 Previous Scans")
    else:
        st.caption("💡 No previous scans were found.")

    for page in pages:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(page)
        with col2:
            if st.button("Delete 🗑️", key=f"delete_{page}"):
                os.remove(os.path.join(pages_dir, page))
                success_message = f"Deleted {page}"
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
                time.sleep(0.3)
                st.rerun()
            else:
                st.error(f"Theme file for '{theme}' not found!")

            st.success(f"Theme applied!")
import streamlit as st
import os

def examples():
        # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### Find assets that you can run tests using Octaprobe!")
    
    with col2:
        with st.popover("💡"):
            st.write("This tool is designed to help you identify potential security issues in your IT resources. It provides a user-friendly interface for scanning and analyzing vulnerabilities.")
            st.warning("Fair Usage Notice: Please use this tool responsibly and ethically. Unauthorized scanning of networks or systems without permission is illegal and unethical. Always ensure you have the necessary permissions before conducting any scans.")    

    col3, col4 = st.columns(2)
    # Define the directory path for assets
    ASSETS_DIRECTORY = os.path.join(os.getcwd(), "examples")
    
    with col3:
        # Hardcoded assets for static analysis
        st.write("#### Static Analysis Binaries")
        with open(f"{ASSETS_DIRECTORY}/helloWorld-Nix.elf", "rb") as file1:
            st.download_button(
            label="Download Static Analysis Binary 1",
            data=file1,
            file_name="helloWorld-Nix.elf",
            mime="application/octet-stream"
            )
        with open(f"{ASSETS_DIRECTORY}/helloWorld-Win.exe", "rb") as file2:
            st.download_button(
            label="Download Static Analysis Binary 2",
            data=file2,
            file_name="helloWorld-Win.exe",
            mime="application/octet-stream"
            )

        # Hardcoded virus files
        st.write("#### Virus Files")
        with open (f"{ASSETS_DIRECTORY}/SampleExecutable.exe", "rb") as file5:
            st.download_button(
            label="Download Virus File 1",
            data=file5,
            file_name="SampleExecutable.exe",
            mime="application/octet-stream"
            )
    
    
    with col4:
        # Hardcoded assets for checksum generation
        st.write("#### Checksum Files")
        with open(f"{ASSETS_DIRECTORY}/text.txt", "rb") as file3:
            st.download_button(
            label="Download Checksum File 1",
            data=file3,
            file_name="checksum_file_1.txt",
            mime="text/plain"
            )
        with open(f"{ASSETS_DIRECTORY}/Image.png", "rb") as file4:
            st.download_button(
            label="Download Checksum File 2",
            data=file4,
            file_name="metadata_image_1.png",
            mime="image/png"
            )
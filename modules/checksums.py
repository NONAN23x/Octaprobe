###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
import hashlib
import base64
import io
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


def generate_checksums():
        
    def get_exif_data(uploaded_file):
        if not uploaded_file.type.startswith("image/"):
            return "File is not an image. EXIF data extraction skipped."
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.read())
        parser = createParser("temp.jpg")
        metadata = extractMetadata(parser)
        if metadata:
            return "\n".join(str(item) for item in metadata.exportPlaintext())
        return "No metadata found."
    def metadata(file):
        if file is not None:
            file_details = {
                "filename": file.name,
                "filetype": file.type,
                "filesize": f"{file.size / (1024 * 1024):.2f} MB"
            }
            return file_details
    def md5sum(file):
        if file.type.startswith("image/"):
            return "file is an image"
        file.seek(0)
        file_content = file.read().rstrip(b'\n')
        file = io.BytesIO(file_content)
        md5_hash = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
        return md5_hash.hexdigest()
    def sha256sum(file):            
        if file.type.startswith("image/"):
            return "file is an image"
        sha256_hash = hashlib.sha256()
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    def sha512sum(file):
        if file.type.startswith("image/"):
            return "file is an image"
        sha512_hash = hashlib.sha512()
        for chunk in iter(lambda: file.read(4096), b""):
            sha512_hash.update(chunk)
        return sha512_hash.hexdigest()
    def base64sum(file):
        if file.type.startswith("image/"):
            return "file is an image"
        file.seek(0)
        file_content = file.read()
        base64_hash = base64.b64encode(file_content).decode('utf-8')
        return base64_hash
    

    # Set the title and description of the app
    
    # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### Generate Checksums, Verify file signatures, Extract metadata.")
    
    with col2:
        with st.popover("💡"):
            st.write("You can upload a file and the module will generate checksums (MD5, SHA-256, SHA-512, Base64) for the file.")
            st.write("You can also upload a signature file to verify the file's signature.")
            st.write("Additionally, you can extract metadata from image files.")
            st.write("This module is useful for file integrity checks, digital forensics, and malware analysis.")
            st.write("Please ensure that the required libraries are installed. If you haven't done so already, please install them by running setup.py")
            st.info("Fair usage notice: This tool is intended for educational and research purposes only. Do not use it for any illegal activities.")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is None:
        st.warning("Waiting for file upload...")
        return
    
    # Printing Metadata first
    with st.expander("File Details"):
        file_details = metadata(uploaded_file)
        exif_data = get_exif_data(uploaded_file)
        st.write(file_details)
        st.divider()
        st.write(exif_data)

    # Allow user to upload a signature file
    with st.expander("Verify file signature"):
        st.badge("Optional")
        signature_file = st.file_uploader("Choose a signature file", key="signature_file", type=["txt", "sig"])
        if signature_file is not None:
            st.write("Signature file uploaded successfully.")
            st.info("Signature verification feature is not yet implemented.")

    # Display checksums in two columns per line
    col1, col2 = st.columns(2, border=True)

    with col1:
        st.write("**SHA-512 Checksum**")
        uploaded_file.seek(0)
        st.code(sha512sum(uploaded_file))

    with col2:
        st.write("**SHA-256 Checksum**")
        uploaded_file.seek(0)
        st.code(sha256sum(uploaded_file))

    col3, col4 = st.columns(2, border=True)

    with col3:
        st.write("**MD5 Checksum**")
        uploaded_file.seek(0)
        st.code(md5sum(uploaded_file))

    with col4:
        st.write("**Base64 Checksum**")
        uploaded_file.seek(0)
        st.code(base64sum(uploaded_file))

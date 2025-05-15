###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
import os
import math
import assets.virustotal_fetch as vt

try:
    import pefile
    from elftools.elf.elffile import ELFFile
    libraryNotFound = False
except ImportError:
    libraryNotFound = True

def analysis():

    def calculate_entropy(data):
        if not data:
            return 0.0
        entropy = 0
        length = len(data)
        occurences = [0] * 256
        for byte in data:
            occurences[byte] += 1
        for count in occurences:
            if count == 0:
                continue
            p_x = count / length
            entropy -= p_x * math.log2(p_x)
        return round(entropy, 3)

    # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### Analyze PE/ELF Binaries to uncover security-relevant information.")
    
    with col2:
        with st.popover("💡"):
            st.write("You can upload a PE or ELF binary file for analysis. The tool will extract information such as entry point, image base, endianness, imported DLLs, sections, and entropy values")
            st.write("This tool analyzes executable files to extract metadata and security-relevant information.")
            st.write("Please ensure that the required libraries are installed. If not, please install them by running setup.py")
            st.info("Note: The analysis may take some time depending on the file size.")

    if libraryNotFound:
        st.warning("The required library 'pefile', 'pyelftools' are not installed. Please install it to proceed.")
        return


    def analyze_pe(file_path):
        pe = pefile.PE(file_path)
        entroy_data = []
        # Calculate entropy for each section and store in entropy_data
        for section in pe.sections:
            data = section.get_data() if hasattr(section, 'get_data') else section.get_data_from_file()
            entropy = calculate_entropy(data)
            entroy_data.append({
                'name': section.Name.decode().strip('\x00'),
                'entropy': entropy
            })

        info1 = {
            "EntryPoint": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
            "ImageBase": hex(pe.OPTIONAL_HEADER.ImageBase),
            "Endianness": "Little Endian" if pe.OPTIONAL_HEADER.Magic == 0x10b else "Big Endian",
            "Imported DLLs": [entry.dll.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT],
            "Sections": [(s.Name.decode().strip('\x00'), hex(s.VirtualAddress)) for s in pe.sections],
        }
        info2 = {
            "Section Entropy": entroy_data,
        }
        return info1, info2
    
    def analyze_elf(file_path):
        with open(file_path, 'rb') as f:
            elf = ELFFile(f)
            entropy_data = {}
            for section in elf.iter_sections():
                data = section.data() if section['sh_size'] > 0 else b''
                entropy = calculate_entropy(data)
                entropy_data[section.name] = entropy
            info1 = {
                "Entry Point": hex(elf.header['e_entry']),
                "Endianness": 'Little' if elf.little_endian else 'Big',
                "Architecture": elf.header['e_machine'],
                "ELF Type": elf['e_type'],
                "Sections": [s.name for s in elf.iter_sections()],
            }
            info2 = {
                "Section Entropy": entropy_data
            }
        return info1, info2
    
    # File uploader for PE or ELF files
    uploaded_file = st.file_uploader("Upload a PE or ELF binary")
    if uploaded_file is None:
        st.warning("Waiting for file upload...")
        return
    elif uploaded_file is not None:
        temp_file_path = os.path.join(os.getcwd(), "assets", "data", uploaded_file.name)
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Determine the file type and analyze accordingly
        try:
            with open(temp_file_path, "rb") as f:
                magic = f.read(4)
                if magic.startswith(b"MZ"):  # PE file magic number
                    # st.toast("Detected PE file format")
                    analysis_col1, analysis_col2 = analyze_pe(temp_file_path)
                elif magic.startswith(b"\x7fELF"):  # ELF file magic number
                    # st.toast("Detected ELF file format")
                    analysis_col1, analysis_col2 = analyze_elf(temp_file_path)
                else:
                    st.error("Unsupported file format")
                    return

            # Display analysis results
            # st.toast("Analysis complete!", icon="✅")
            with st.expander("Analysis Results"):
                # col1, col2 = st.columns([0.8, 0.9], vertical_alignment="center")
                col3, col4 = st.columns(2, border=True)
                # col1.info("An extropy value of 7.5 or higher is considered suspicious.")
                # col2.button("Download Report", key="download_report")
                # if col2:
                    # analysis_report = ReportGenerator(uploaded_file.name)
                    # analysis_report.generate_malware_analysis_report({**analysis_col1, **analysis_col2})
                col3.json(analysis_col1); col4.json(analysis_col2)

        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
    
def virus_analysis():

    api_key = os.getenv("VIRUSTOTAL_API_KEY")
    if not api_key:
        st.write("VirusTotal API key not found. Please set the 'VIRUSTOTAL_API_KEY' environment variable.")
        st.warning("Note: This is a demo version; to use the Virustotal feature, you need to run the project on your local system and supply your own API key.")
        return
    
    def send_to_virustotal(file_path):
        result, chart, hashes, timetaken = vt.virustotal_analysis(file_path)
        st.write(result)
        if result:
            cols1, cols2, cols3 = st.columns(3, border=True)
            with cols1:
                st.write("SHA256 Hash:")
                st.code(hashes.get("sha256"))
            with cols2:
                st.write("MD5 Hash:")
                st.code(hashes.get("md5"))
            with cols3:
                st.write("sha1 Hash:")
                st.code(hashes.get("sha1"))
            st.bar_chart(chart)
            col6, col7 = st.columns([0.8, 0.2])
            col6.success(f"VirusTotal analysis completed successfully ({timetaken:.2f})")
            if col7.button("Refresh"):
                st.rerun()
        else:
            st.error("VirusTotal analysis failed.")
    
        # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### Detect malware using VirusTotal API.")
    
    with col2:
        with st.popover("💡"):
            st.write("You can upload a file for analysis.")
            st.write("If the results came out as queue, please wait for a while and refresh the page.")
            st.info("Note: Virustotal uses more than 50 antivirus engine to perform analysis on the file, so it may take very longer processing times, it is adviced to wait atleast 30 seconds before refreshing. As the tool timeouts after 30 seconds by itself.")
            st.warning("Remember to hit x on the uploaded file to remove it after analysis, before proceeding to next features.")
    
    # File uploader for PE or ELF files
    uploaded_file = st.file_uploader("Upload a file", key="vt_file")

    if uploaded_file is None:
        st.warning("Waiting for file upload...")
        return
    elif uploaded_file:
        temp_file_path = os.path.join(os.getcwd(), "assets", "data", uploaded_file.name)
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())
            with st.spinner("Performing VirusTotal analysis..."):
                send_to_virustotal(temp_file_path)

import streamlit as st
try:
    import pefile
    from elftools.elf.elffile import ELFFile
    libraryNotFound = False
except ImportError:
    libraryNotFound = True

def analysis():
    st.subheader("Malware Analysis")
    st.write("Perform static malware analysis on Windows or Linux executables")

    if libraryNotFound:
        st.warning("The required library 'pefile', 'pyelftools' are not installed. Please install it to proceed.")
        return
    

    def analyze_pe(file_path):
        pe = pefile.PE(file_path)
        info = {
            "EntryPoint": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
            "ImageBase": hex(pe.OPTIONAL_HEADER.ImageBase),
            "Imported DLLs": [entry.dll.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT],
            "Sections": [(s.Name.decode().strip(), hex(s.VirtualAddress)) for s in pe.sections],
        }
        return info
    
    def analyze_elf(file_path):
        with open(file_path, 'rb') as f:
            elf = ELFFile(f)
            info = {
                "Architecture": elf.header['e_machine'],
                "Entry Point": hex(elf.header['e_entry']),
                "Endianness": 'Little' if elf.little_endian else 'Big',
                "ELF Type": elf['e_type'],
                "Sections": [s.name for s in elf.iter_sections()]
            }
        return info
    
    # File uploader for PE or ELF files
    uploaded_file = st.file_uploader("Upload a PE or ELF binary", type=["exe", "dll", "sys", "elf"])
    if uploaded_file is None:
        st.warning("Waiting for file upload...")
        return
    elif uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_file_path = f"/tmp/{uploaded_file.name}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Determine the file type and analyze accordingly
        try:
            with open(temp_file_path, "rb") as f:
                magic = f.read(4)
                if magic.startswith(b"MZ"):  # PE file magic number
                    st.info("Detected PE file format")
                    analysis_result = analyze_pe(temp_file_path)
                elif magic.startswith(b"\x7fELF"):  # ELF file magic number
                    st.info("Detected ELF file format")
                    analysis_result = analyze_elf(temp_file_path)
                else:
                    st.error("Unsupported file format")
                    return

            # Display analysis results
            st.json(analysis_result)

        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
    

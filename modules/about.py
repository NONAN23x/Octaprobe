import streamlit as st

def about():
    # About section content
    st.subheader("About Octaprobe")
    st.write(
        """
        **Octaprobe** is a security assessment tool designed to help security professionals and developers identify potential vulnerabilities in their systems. 
        It leverages various technologies and libraries to provide a comprehensive scanning experience.
        The tool is built using Python and Streamlit, making it easy to use and deploy.
        The main features of Octaprobe include:
        - **Basic Scan**: Quickly identify open ports and services running on a target system.
        - **Advanced Scan**: Perform a more in-depth analysis of the target system, including service version detection and OS fingerprinting.
        - **Web Scan**: Discover web application endpoints and potential vulnerabilities.
        - **Malware Analysis**: Analyze files for potential malware using various techniques.
        - **Checksum Generation**: Generate checksums for files to verify their integrity.
        - **Assistant**: A built-in assistant to help users navigate the tool and provide additional information.
        """
    )
    
    st.subheader("Technologies Used")
    st.write(
        """
        - **Python**: The primary programming language used for development.
        - **Streamlit**: A framework for building web applications in Python.
        - **Nmap**: A powerful network scanning tool used for discovering hosts and services on a computer network.
        - **Ollama**: A library for building and deploying machine learning models.
        - **Shodan**: A search engine for Internet-connected devices.
        """
    )
    st.subheader("License")
    st.write(
        """
        This project is licensed under the GNU General Public License v3.0.
        You can freely use, modify, and distribute this software under the terms of the license.
        For more details, please refer to the [LICENSE](LICENSE) file in the repository.
        """
    )
    st.subheader("Contributing")
    st.write(
        """
        Contributions are welcome! If you find a bug or have a feature request, please open an issue
        or submit a pull request on GitHub.
        """)
    
    st.write("""
        References:
        - [Streamlit Documentation](https://docs.streamlit.io/)
        - [Nmap Documentation](https
://nmap.org/docs/)
        - [LangChain Documentation](https://docs.langchain.com/)
        - [VulnersAPI Documentation](https://vulners.com/)
        - [Python Documentation](https://docs.python.org/3/)
             
             """)
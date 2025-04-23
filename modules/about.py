import streamlit as st

def about():
    # About section content
    st.title("About Octaprobe")
    st.write(
        """
        **Octaprobe** is a vulnerability scanner designed to help security professionals and developers identify potential vulnerabilities in their systems. 
        It leverages various technologies and libraries to provide a comprehensive scanning experience.
        """
    )
    
    st.subheader("Technologies Used")
    st.write(
        """
        - **Python**: The primary programming language used for development.
        - **Streamlit**: A framework for building web applications in Python.
        - **Nmap**: A powerful network scanning tool used for discovering hosts and services on a computer network.
        - **LangChain**: A framework for developing applications powered by language models.
        - **VulnersAPI**: An API that provides access to vulnerability data.
        """
    )
    st.subheader("License")
    st.write(
        """
        This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
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
###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
try :
    from ollama import ChatResponse
    from ollama import chat
    ollamaNotFound = False
except ImportError:
    ollamaNotFound = True

def assistant():

    if ollamaNotFound:
        st.error("Ollama (module or service) is not installed. Please install it to use this feature.")
        return
    

    # Create two columns with specified width ratio
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### OctaBot is a friendly assistant that can help you with various tasks related to Octaprobe and Security Best Practises.")
    
    with col2:
        with st.popover("💡"):
            st.write("You can ask questions like: `How to use the tool?`, `What features are available?`, `Can you help me with a specific task?`. Please ensure that the required libraries are installed. If not, please install them by running setup.py")
            st.info("Note: The assistant is powered by Ollama. Ensure that the Ollama service is running for the assistant to function properly.")
            st.write("If you encounter any issues, please check the Ollama Documentation for troubleshooting steps.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            # Provide a simple response based on the user's question
            if "what" in prompt.lower():
                response = "OctaProbe is a lightweight and efficient vulnerability scanner designed to identify security weaknesses in various systems. Built with Python and leveraging modern frameworks like Streamlit, it provides an intuitive interface for users to perform scans and analyze results. OctaProbe supports multiple operating systems, making it a versatile tool for developers, security analysts, and IT professionals."
            elif "how" in prompt.lower():
                response = "To use Octaprobe, follow the setup instructions in the README.md file on our GitHub repository."
            elif "why" in prompt.lower():
                response = "Octaprobe helps in identifying security vulnerabilities efficiently. Check out the GitHub repository for more details."
            else:
                response = "I'm here to assist with Octaprobe-related queries. Visit our GitHub repository to learn more!"

            # Display the response in the chat message container
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Add a link button to redirect to the GitHub repository
            st.link_button("Visit GitHub Repository", url="https://github.com/NONAN23x/Octaprobe")

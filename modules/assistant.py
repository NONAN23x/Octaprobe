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
    
    def chat_with_OctaBot(userInput: str):
        try:
            response: ChatResponse = chat(model='OctaBot', stream=True, messages=[
            {
                'role': 'user',
                'content': userInput,
            },
            ])
            for chunk in response:
                yield chunk['message']['content']
        except Exception as e:
            st.error(f"Is ollama running?: {e}")

    # Create two columns with specified width ratio
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### The OctaBot is designed to provide helpful responses and guidance based on your input. Feel free to ask anything related to the tool or its features")
    
    with col2:
        with st.popover("💡"):
            st.write("You can ask questions like: 'How to use the tool?', 'What features are available?', 'Can you help me with a specific task?'. Please ensure that the required libraries are installed. If not, please install them by running setup.py")
            st.info("Note: The assistant is powered by Ollama. Ensure that the Ollama service is running for the assistant to function properly.")
            st.write("If you encounter any issues, please check the Ollama installation and ensure that the model is available.")

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

        stream = chat_with_OctaBot(prompt)

        with st.chat_message("assistant"):
            # Display the response in the chat message container

            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})

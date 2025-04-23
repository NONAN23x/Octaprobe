import streamlit as st
try :
    from ollama import ChatResponse
    from ollama import chat
    ollamaNotFound = False
except ImportError:
    ollamaNotFound = True


def assistant():

    if ollamaNotFound:
        st.error("Ollama is not installed. Please install it to use this feature.")
        return
    
    def chat_with_OctaBot(userInput: str):
        response: ChatResponse = chat(model='OctaBot', stream=True, messages=[
        {
            'role': 'user',
            'content': userInput,
        },
        ])
        for chunk in response:
            yield chunk['message']['content']

    # chat_with_gemma()
    st.title("Octaprobe Assistant")

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


    if prompt:
        stream = chat_with_OctaBot(prompt)

        with st.chat_message("assistant"):
            # Display the response in the chat message container

            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})

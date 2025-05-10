###############################################################################
# Octaprobe Security Scanner - Security Analysis Suite
# Secure, Scalable, Scanning Infrastructure
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import streamlit as st
import json
import requests


def repeater():

    def sanitize_url(url):
        # Check if the URL is empty
        if not url:
            return False

        # Remove leading/trailing spaces and ensure no spaces in the middle
        sanitized_url = url.strip().replace(" ", "")

        # Validate URL structure
        if not sanitized_url.startswith(("http://", "https://")):
            return False

        # Check for irrelevant characters
        allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=%"
        if any(char not in allowed_chars for char in sanitized_url):
            return False

        return True
    
    def send_api_request(url, method, headers_str, payload_str):
        try:
            # Default headers
            default_headers = {"User-Agent": "APITester"}

            # Parse headers and payload with fallback
            try:
                headers = {**default_headers, **json.loads(headers_str or "{}")}
            except json.JSONDecodeError:
                return st.error("Invalid JSON in headers.")

            try:
                payload = json.loads(payload_str or "{}")
            except json.JSONDecodeError:
                return st.error("Invalid JSON in payload.")

            # Send request
            response = requests.request(method, url, headers=headers, json=payload if method == "POST" else None)

            # Display
            st.subheader("Response")
            if 200 <= response.status_code < 300:
                st.badge(f"Status Code: {response.status_code}", color="green")
            elif 400 <= response.status_code < 500:
                st.badge(f"Status Code: {response.status_code}", color="red")
            else:
                st.badge(f"Status Code: {response.status_code}", color="yellow")

            if response.headers.get("Content-Type", "").startswith("application/json"):
                with st.expander("Response JSON"):
                    st.json(response.json())
            else:
                with st.expander("Response JSON"):
                    st.text(response.text)

            # Optional: show response headers and elapsed time
            with st.expander("Response Headers"):
                st.json(dict(response.headers))
            st.caption(f"Time taken: {response.elapsed.total_seconds()}s")

        except Exception as e:
            with st.expander(label="An error occured, is the endpoint correct?", icon="🚨"):
                st.warning(f"{e}")


    # Create two columns with specified width ratio
    col1, col2 = st.columns([0.9, 0.1])
    
    with col1:
        st.write("#### Test Functionality of APIs by sending Modified Requests and Inspecting Responses.")
    
    with col2:
        with st.popover("💡"):
            st.write("The tool supports GET and POST methods, and you can specify headers and payloads in JSON format")
            st.warning("Fair Usage Notice: Please use this tool responsibly and avoid sending excessive requests to any API. This tool is intended for educational and testing purposes only.")
            st.write("Ensure that you have permission to test the API and that you are not violating any terms of service.")

    # Columns for URL and Method
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        url = st.text_input("Endpoint", placeholder="http://example.com/api/v1/")
    with col2:
        method = st.selectbox("Method", ["GET", "POST"])

    # Headers and Payload in a single line using columns
    col3, col4 = st.columns([0.5, 0.5])
    with col3:
        headers_str = st.text_area("Headers (JSON format)", '{"Content-Type": "application/json"}')
    with col4:
        if method == "POST":
            payload_str = st.text_area("Payload (JSON format)", '{\n"key": "value"\n}')
        else:
            payload_str = "{}"  # Default empty payload for non-POST methods

    send_request = st.button("Send Request")
    
    st.divider()
    # Send button
    if send_request:
        if sanitize_url(url): # Check if URL is valid
            with st.expander("Demo version!"):
                st.write("This feature is not available on the demo version. Please check the full version for more details.")
                st.toast("Please check the full version on GitHub!", icon="🔥")
                st.link_button("Grab the full project from Github!", url="https://github.com/NONAN23x/Octaprobe")
        else:
            st.error("Invalid URL. Please check the format and try again.")
    else:
        st.info("Fill in the details and click 'Send Request' to test the API.")

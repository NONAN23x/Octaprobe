import streamlit as st
import os

def settings():
    st.subheader("Settings")
    st.write("Configure your scan settings here.")

    # Directory containing the pages
    pages_dir = os.path.join(os.getcwd(), "pages")

    # List all files in the pages directory
    if os.path.exists(pages_dir):
        pages = [f for f in os.listdir(pages_dir) if os.path.isfile(os.path.join(pages_dir, f))]
    else:
        pages = []

    st.divider()
    success_message = None

    if pages:
        st.caption("📁 Previous Scan")
    else:
        st.caption("💡 No previous scans were found.")

    for page in pages:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(page)
        with col2:
            if st.button("Delete 🗑️", key=f"delete_{page}"):
                os.remove(os.path.join(pages_dir, page))
                success_message = f"Deleted {page}"

    if success_message:
        st.success(success_message)

    st.divider()

    "st.session_state", st.write(st.session_state)
import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.header("Navigation")

        st.success("Sprint 3")

        st.write("✅ Product Master")
        st.write("🚧 Demand Planning")
        st.write("🚧 Reports")
        st.write("🚧 AI Assistant")

        st.divider()

        st.info("Version 1.0")

import streamlit as st


def render_header():

    st.set_page_config(
        page_title="Demand Copilot",
        page_icon="📈",
        layout="wide"
    )

    st.title("📈 Demand Copilot")
    st.caption("AI Powered Demand Planning Platform")

    st.divider()

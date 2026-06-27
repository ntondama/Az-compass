import streamlit as st


def render_header():
    st.set_page_config(
        page_title="Demand Planning Copilot",
        page_icon="📈",
        layout="wide"
    )

    st.title("📈 Demand Planning Copilot")
    st.markdown("### AI Powered Retail Demand Planning")
    st.divider()

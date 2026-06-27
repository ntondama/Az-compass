import streamlit as st


def render_sidebar():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "",
        [
            "Dashboard",
            "Product Catalog",
            "Demand Simulator",
            "Reports",
            "AI Copilot"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.success("Sprint 3")
    st.sidebar.markdown("---")
    st.sidebar.caption("Version 2.0")

    return page

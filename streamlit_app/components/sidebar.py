import streamlit as st


def render_sidebar():

    st.sidebar.title("📈 Demand Copilot")

    page = st.sidebar.radio(
        "Navigation",
        (
            "Dashboard",
            "Product Catalog",
            "Demand Simulator",
            "Reports",
            "AI Copilot",
        ),
        index=0,
    )

    st.sidebar.markdown("---")
    st.sidebar.success("Sprint 3")
    st.sidebar.caption("Version 2.0")

    return page

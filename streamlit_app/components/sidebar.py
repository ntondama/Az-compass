import streamlit as st


def render_sidebar():

    st.sidebar.image(
        "https://img.icons8.com/color/96/combo-chart--v1.png",
        width=60,
    )

    st.sidebar.title("Demand Copilot")

    st.sidebar.caption("Retail Demand Planning")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Product Catalog",
            "Demand Simulator",
            "Reports",
            "AI Copilot",
        ],
    )

    st.sidebar.markdown("---")

    st.sidebar.success("Sprint 3 Demo")

    st.sidebar.markdown(
        """
### Current Modules

✅ Product Catalog

✅ Demand Simulator

🚧 AI Copilot

🚧 Reports
"""
    )

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 2.0")

    return page

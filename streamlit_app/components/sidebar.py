import streamlit as st


def render_sidebar():

    st.sidebar.image(
        "https://img.icons8.com/color/96/combo-chart--v1.png",
        width=60,
    )

    st.sidebar.title("Demand Copilot")

    st.sidebar.caption("AI Powered Demand Planning")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📈 Planning Workspace",
            "📦 Product Catalog",
            "📊 Reports",
            "🤖 AI Copilot",
        ],
    )

    st.sidebar.markdown("---")

    st.sidebar.success("Sprint 5")

    st.sidebar.markdown(
        """
### Available Modules

✅ Dashboard

✅ Planning Workspace

✅ Product Catalog

🚧 Reports

🚧 AI Copilot
"""
    )

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 3.0")

    return page

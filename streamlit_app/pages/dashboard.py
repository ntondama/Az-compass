import streamlit as st

from components.dashboard_cards import show_dashboard_cards


def show_dashboard():

    st.subheader("🏠 Dashboard")

    show_dashboard_cards()

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📦 Product Catalog")

    with col2:
        st.button("📈 Run Simulation")

    with col3:
        st.button("📑 View Reports")

    st.divider()

    st.subheader("🤖 AI Insights")

    st.info(
        "AI recommendations will appear here after Azure AI integration."
    )

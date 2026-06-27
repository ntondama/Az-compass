import streamlit as st
from services.csv_service import CSVService


def show_dashboard():

    service = CSVService()

    st.title("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Products", service.get_total_products())

    col2.metric("Categories", service.get_total_categories())

    col3.metric("Active Products", service.get_active_products())

    st.divider()

    st.subheader("Welcome")

    st.info(
        """
Welcome to Demand Copilot.

✔ Product Catalog

✔ Demand Simulator

✔ Reports

✔ AI Copilot
"""
    )

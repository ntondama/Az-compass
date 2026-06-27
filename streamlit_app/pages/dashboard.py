import streamlit as st
from services.csv_service import CSVService

service = CSVService()


def show_dashboard():

    st.title("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Products",
        service.get_total_products()
    )

    col2.metric(
        "Categories",
        service.get_total_categories()
    )

    col3.metric(
        "Active Products",
        service.get_active_products()
    )

    st.markdown("---")

    st.subheader("Demand Planning Overview")

    st.info(
        """
        Welcome to Demand Copilot.

        This dashboard will provide

        • Product Planning

        • Demand Simulation

        • AI Insights

        • Business Reports
        """
    )

import streamlit as st
from services.csv_service import CSVService


def show_dashboard_cards():

    service = CSVService()

    total_products = service.get_total_products()
    total_categories = service.get_total_categories()
    active_products = service.get_active_products()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📦 Total Products",
            value=total_products
        )

    with col2:
        st.metric(
            label="🏷 Categories",
            value=total_categories
        )

    with col3:
        st.metric(
            label="✅ Active Products",
            value=active_products
        )

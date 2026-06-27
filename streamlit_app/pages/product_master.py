import streamlit as st

from services.csv_service import CSVService


def show_product_master():

    st.subheader("📦 Product Master")

    csv_service = CSVService()

    products = csv_service.load_products()

    st.dataframe(
        products,
        use_container_width=True,
        hide_index=True
    )

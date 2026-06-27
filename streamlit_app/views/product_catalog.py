import streamlit as st
from services.csv_service import CSVService


def show_product_catalog():

    service = CSVService()

    st.title("📦 Product Catalog")

    products = service.load_products()

    st.dataframe(
        products,
        use_container_width=True,
        hide_index=True,
    )

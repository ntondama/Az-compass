import streamlit as st
from services.csv_service import CSVService

service = CSVService()


def show_product_master():

    st.title("📦 Product Catalog")

    df = service.load_products()

    st.dataframe(
        df,
        use_container_width=True
    )

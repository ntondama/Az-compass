import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

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

import streamlit as st
from services.csv_service import CSVService

service = CSVService()


def show_product_catalog():

    st.title("📦 Product Catalog")
    st.caption("Manage products used for demand planning")

    df = service.load_products()

    # --------------------------
    # Filters
    # --------------------------

    c1, c2, c3 = st.columns([3, 2, 1])

    with c1:
        search = st.text_input(
            "🔍 Search Product",
            placeholder="Search by Product Name...",
        )

    with c2:
        categories = ["All"] + sorted(df["category"].unique().tolist())

        selected_category = st.selectbox(
            "Category",
            categories,
        )

    with c3:
        st.write("")
        st.write("")
        st.button(
            "➕ Add Product",
            use_container_width=True,
        )

    # --------------------------
    # Filtering
    # --------------------------

    filtered = df.copy()

    if search:

        filtered = filtered[
            filtered["product_name"]
            .str.contains(search, case=False)
        ]

    if selected_category != "All":

        filtered = filtered[
            filtered["category"] == selected_category
        ]

    st.markdown("---")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=450,
    )

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric("Products", len(filtered))
    c2.metric("Categories", filtered["category"].nunique())
    c3.metric(
        "Active",
        len(filtered[filtered["status"] == "Active"]),
    )

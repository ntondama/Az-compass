import streamlit as st
import pandas as pd

from services.csv_service import CSVService
from components.dashboard_cards import metric_card

service = CSVService()


def show_dashboard():

    st.title("📊 Executive Dashboard")
    st.caption("AI-powered demand planning overview")

    df = service.load_products()

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Products",
            len(df),
            "+2 this month",
            "📦",
        )

    with col2:
        metric_card(
            "Categories",
            df["category"].nunique(),
            "Stable",
            "🗂️",
        )

    with col3:
        metric_card(
            "Active Products",
            len(df[df["status"] == "Active"]),
            "100%",
            "✅",
        )

    with col4:
        metric_card(
            "Demand Health",
            "96%",
            "+4%",
            "📈",
        )

    st.markdown("---")

    # ==========================
    # MAIN LAYOUT
    # ==========================

    left, right = st.columns([3, 1])

    with left:

        st.subheader("Product Catalog Overview")

        st.dataframe(
            df,
            use_container_width=True,
            height=420,
        )

    with right:

        st.subheader("Planning Alerts")

        st.warning("Low inventory forecast for Dairy")

        st.info("2 new products awaiting approval")

        st.success("Demand forecast refreshed")

        st.error("1 simulation pending")

        st.markdown("---")

        st.subheader("AI Recommendations")

        st.markdown("""
- Increase Beverage forecast

- Review Dairy pricing

- Optimize Snack inventory

- Simulate next month's demand

- Review inactive products
""")

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Demand Trend")

        trend = pd.DataFrame(
            {
                "Week": [
                    "W1",
                    "W2",
                    "W3",
                    "W4",
                    "W5",
                    "W6",
                ],
                "Demand": [
                    110,
                    125,
                    118,
                    140,
                    150,
                    162,
                ],
            }
        )

        st.line_chart(
            trend.set_index("Week")
        )

    with c2:

        st.subheader("Category Distribution")

        category = (
            df["category"]
            .value_counts()
        )

        st.bar_chart(category)

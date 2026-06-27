import streamlit as st
import pandas as pd


def show_reports():

    st.title("📑 Business Reports")
    st.caption("Demand Planning Reporting Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Forecast Accuracy", "96%")
    col2.metric("Revenue", "$2.4M")
    col3.metric("Service Level", "98%")

    st.divider()

    chart = pd.DataFrame(
        {
            "Month": [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
            ],
            "Sales": [
                110,
                130,
                125,
                145,
                155,
                170,
            ],
        }
    )

    st.subheader("Monthly Sales Trend")

    st.line_chart(
        chart.set_index("Month")
    )

    st.divider()

    st.subheader("Downloads")

    c1, c2 = st.columns(2)

    with c1:
        st.button(
            "📄 Download Report",
            use_container_width=True,
        )

    with c2:
        st.button(
            "📊 Export Dashboard",
            use_container_width=True,
        )

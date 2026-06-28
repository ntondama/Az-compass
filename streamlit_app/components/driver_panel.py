import streamlit as st


def render_driver_panel():

    st.subheader("📊 Driver Configuration")

    left, right = st.columns(2)

    with left:

        trend = st.slider(
            "Trend (%)",
            -20,
            20,
            0,
        )

        distribution = st.slider(
            "Distribution (%)",
            -20,
            20,
            0,
        )

        pricing = st.slider(
            "Pricing (%)",
            -20,
            20,
            0,
        )

    with right:

        trade_spend = st.slider(
            "Trade Spend (%)",
            -20,
            20,
            0,
        )

        inventory = st.slider(
            "Inventory (%)",
            -20,
            20,
            0,
        )

    return {
        "trend": trend,
        "distribution": distribution,
        "pricing": pricing,
        "trade_spend": trade_spend,
        "inventory": inventory,
    }

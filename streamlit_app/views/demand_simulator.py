import streamlit as st


def show_demand_simulator():

    st.title("📈 Demand Simulator")
    st.caption("Simulate demand planning driver changes")

    left, right = st.columns([1, 1])

    with left:

        st.subheader("Planning Drivers")

        distribution = st.slider(
            "Distribution %",
            -20,
            20,
            0,
        )

        trend = st.slider(
            "Trend %",
            -20,
            20,
            0,
        )

        pricing = st.slider(
            "Pricing %",
            -20,
            20,
            0,
        )

        velocity = st.slider(
            "Velocity %",
            -20,
            20,
            0,
        )

        trade_spend = st.slider(
            "Trade Spend %",
            -20,
            20,
            0,
        )

        st.button(
            "🚀 Run Simulation",
            use_container_width=True,
        )

    with right:

        st.subheader("Business Impact")

        volume = trend + distribution // 2

        shipment = volume - 1

        gsv = pricing + volume

        st.metric("Volume", f"{volume}%")

        st.metric("Shipment", f"{shipment}%")

        st.metric("GSV", f"{gsv}%")

        st.metric("NSV", f"{gsv-1}%")

        st.metric("Fund Balance", f"{100-gsv}%")

        st.success("Simulation completed successfully.")

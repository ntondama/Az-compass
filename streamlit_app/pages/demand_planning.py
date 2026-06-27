import streamlit as st


def show_demand_planning():

    st.title("📈 Demand Simulator")

    st.info("Demand Planning Agent UI will be implemented tomorrow.")

    col1, col2 = st.columns(2)

    with col1:

        st.number_input(
            "Distribution %",
            value=10
        )

        st.number_input(
            "Trend %",
            value=2
        )

        st.number_input(
            "Price %",
            value=1
        )

    with col2:

        st.metric(
            "Forecast Volume",
            "12500"
        )

        st.metric(
            "Revenue",
            "$240000"
        )

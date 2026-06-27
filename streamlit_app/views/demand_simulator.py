import streamlit as st


def show_demand_simulator():

    st.title("📈 Demand Simulator")

    st.number_input("Selling Price", value=100)

    st.number_input("Market Trend", value=2)

    st.number_input("Marketing Budget", value=20)

    if st.button("Run Simulation"):

        st.success(
            "Simulation Engine will be implemented tomorrow."
        )

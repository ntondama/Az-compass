import streamlit as st


def show_demand_simulator():

    st.subheader("📈 Demand Simulator")

    st.selectbox(

        "Category",

        [

            "Dairy",

            "Bakery",

            "Grocery",

            "Beverages"

        ]

    )

    st.text_input("Product")

    st.slider(

        "Selling Price",

        0,

        500,

        100

    )

    st.slider(

        "Market Trend",

        -20,

        20,

        0

    )

    st.slider(

        "Marketing Budget",

        0,

        100,

        20

    )

    if st.button("Run Simulation"):

        st.success(

            "Simulation Engine will be integrated in Sprint 4."

        )

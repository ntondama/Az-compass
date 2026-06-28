import streamlit as st

from agents.demand_agent import DemandAgent


def show_demand_simulator():

    st.title("📈 Demand Simulator")
    st.caption("Run demand planning scenarios")

    agent = DemandAgent()

    st.subheader("Scenario Inputs")

    col1, col2 = st.columns(2)

    with col1:

        category = st.selectbox(
            "Product Category",
            [
                "Dairy",
                "Bakery",
                "Grocery",
                "Beverages",
                "Snacks",
            ],
        )

        scenario = st.text_input(
            "Scenario Name",
            "Summer Promotion",
        )

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

    with col2:

        pricing = st.slider(
            "Pricing (%)",
            -20,
            20,
            0,
        )

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

    st.divider()

    if st.button(
        "🚀 Run Simulation",
        use_container_width=True,
    ):

        result = agent.simulate(
            {
                "trend": trend,
                "distribution": distribution,
                "pricing": pricing,
                "trade_spend": trade_spend,
                "inventory": inventory,
            }
        )

        st.success("Simulation completed successfully.")

        st.subheader("Simulation KPIs")

        c1, c2, c3 = st.columns(3)

        c1.metric("Volume", f"{result['Volume']:.1f}%")
        c2.metric("Shipment", f"{result['Shipment']:.1f}%")
        c3.metric("GSV", f"{result['GSV']:.1f}%")

        c4, c5, c6 = st.columns(3)

        c4.metric("NSV", f"{result['NSV']:.1f}%")
        c5.metric("Spend", f"{result['Spend']:.1f}%")
        c6.metric("Fund Balance", f"{result['Fund Balance']:.1f}%")

        st.divider()

        st.subheader("AI Business Summary")

        st.info(
            f"""
Scenario **{scenario}** for **{category}**

• Trend changed by **{trend}%**

• Distribution changed by **{distribution}%**

• Pricing changed by **{pricing}%**

• Trade Spend changed by **{trade_spend}%**

• Inventory changed by **{inventory}%**

Expected outcome:

• Volume: **{result['Volume']:.1f}%**

• Shipment: **{result['Shipment']:.1f}%**

• GSV: **{result['GSV']:.1f}%**

• NSV: **{result['NSV']:.1f}%**

• Spend: **{result['Spend']:.1f}%**

• Fund Balance: **{result['Fund Balance']:.1f}%**
"""
        )

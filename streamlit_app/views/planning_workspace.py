import streamlit as st

from components.driver_panel import render_driver_panel
from components.simulation_panel import render_simulation_panel


def show_planning_workspace():

    st.title("📈 Planning Workspace")

    st.caption(
        "Create and evaluate demand planning scenarios"
    )

    st.divider()

    # --------------------------------------------------
    # Scenario Information
    # --------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        category = st.selectbox(
            "Category",
            [
                "Dairy",
                "Bakery",
                "Beverages",
                "Grocery",
                "Snacks",
            ],
        )

    with c2:
        product = st.selectbox(
            "Product",
            [
                "Milk",
                "Bread",
                "Tea Powder",
                "Rice",
            ],
        )

    with c3:
        scenario = st.text_input(
            "Scenario Name",
            "Summer Promotion",
        )

    st.divider()

    # --------------------------------------------------
    # Driver Configuration
    # --------------------------------------------------

    drivers = render_driver_panel()

    st.divider()

    # --------------------------------------------------
    # Simulation
    # --------------------------------------------------

    result = render_simulation_panel(drivers)

    st.divider()

    # --------------------------------------------------
    # AI Recommendation
    # --------------------------------------------------

    if result:

        st.subheader("🤖 AI Recommendation")

        st.success(
            f"""
Scenario **{scenario}** for **{category}** has been evaluated.

Key Highlights

• Volume : {result['Volume']:.1f}%

• Shipment : {result['Shipment']:.1f}%

• GSV : {result['GSV']:.1f}%

• NSV : {result['NSV']:.1f}%

Recommendation

The scenario shows the expected impact based on the selected demand drivers.
Review the KPI values before saving this scenario.
"""
        )

    else:

        st.info("Run a simulation to receive AI recommendations.")

    st.divider()

    # --------------------------------------------------
    # Save Scenario
    # --------------------------------------------------

    st.button(
        "💾 Save Scenario",
        use_container_width=True,
    )

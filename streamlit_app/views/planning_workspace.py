import streamlit as st

from services.csv_service import CSVService

from components.driver_panel import render_driver_panel
from components.simulation_panel import render_simulation_panel
from components.save_panel import render_save_panel


def show_planning_workspace():

    service = CSVService()

    st.title("📈 Planning Workspace")

    st.caption(
        "Create, simulate and save demand planning scenarios."
    )

    st.divider()

    categories = service.get_categories()

    c1, c2, c3 = st.columns(3)

    with c1:

        category = st.selectbox(
            "Category",
            categories,
        )

    with c2:

        products = service.get_products_by_category(category)

        product = st.selectbox(
            "Product",
            products,
        )

    with c3:

        scenario = st.text_input(
            "Scenario Name",
            "Summer Promotion",
        )

    st.divider()

    # ---------------- Driver Configuration ----------------

    drivers = render_driver_panel()

    st.session_state["drivers"] = drivers

    st.divider()

    # ---------------- Simulation ----------------

    result = render_simulation_panel(drivers)

    if result:

        st.session_state["scenario_name"] = scenario
        st.session_state["category"] = category
        st.session_state["product"] = product

    st.divider()

    # ---------------- AI Recommendation ----------------

    if result:

        st.subheader("🤖 AI Recommendation")

        st.success(
            f"""
### Scenario Summary

Scenario **{scenario}** has been evaluated successfully.

**Category:** {category}

**Product:** {product}

---

### KPI Summary

- Volume : {result['Volume']:.1f}%

- Shipment : {result['Shipment']:.1f}%

- GSV : {result['GSV']:.1f}%

- NSV : {result['NSV']:.1f}%

- Spend : {result['Spend']:.1f}%

- Fund Balance : {result['Fund Balance']:.1f}%

---

Recommendation:

The selected demand drivers indicate positive business impact.
Review KPI values before saving the scenario.
"""
        )

    else:

        st.info(
            "Run a simulation to generate AI recommendations."
        )

    st.divider()

    # ---------------- Save Scenario ----------------

    render_save_panel(
        scenario_name=scenario,
        category=category,
        product=product,
        drivers=drivers,
        result=result,
    )

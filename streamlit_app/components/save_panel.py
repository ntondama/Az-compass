import streamlit as st
from datetime import datetime

from models.scenario import Scenario
from services.scenario_service import ScenarioService


def render_save_panel(
    scenario_name,
    category,
    product,
    drivers,
    result,
):

    result = st.session_state.get("simulation_result")

    if result is None:
        st.info("Run a simulation before saving.")
        return

    st.subheader("💾 Save Scenario")

    if st.button(
        "💾 Save Scenario",
        width="stretch",
    ):

        scenario = Scenario(
            scenario_name=scenario_name,
            category=category,
            product=product,
            trend=drivers["trend"],
            distribution=drivers["distribution"],
            pricing=drivers["pricing"],
            trade_spend=drivers["trade_spend"],
            inventory=drivers["inventory"],
            volume=result["Volume"],
            shipment=result["Shipment"],
            gsv=result["GSV"],
            nsv=result["NSV"],
            spend=result["Spend"],
            fund_balance=result["Fund Balance"],
            created_time=datetime.now(),
        )

        service = ScenarioService()

        service.save(scenario)

        st.success("✅ Scenario saved successfully.")

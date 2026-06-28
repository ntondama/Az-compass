import streamlit as st

from services.scenario_service import ScenarioService


service = ScenarioService()


def show_scenario_manager():

    st.title("📋 Scenario Manager")

    st.caption(
        "Saved Demand Planning Scenarios"
    )

    df = service.load()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )

    st.metric(
        "Saved Scenarios",
        len(df),
    )

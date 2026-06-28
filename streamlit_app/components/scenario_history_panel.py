import streamlit as st

from services.scenario_service import ScenarioService


def render_scenario_history():

    st.subheader("📂 Saved Scenarios")

    service = ScenarioService()

    df = service.load()

    if df.empty:

        st.info("No scenarios have been saved yet.")

        return

    st.dataframe(
        df,
        width="stretch",
        hide_index=True,
    )

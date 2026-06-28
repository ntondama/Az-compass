import streamlit as st

from agents.orchestrator import Orchestrator


def render_simulation_panel(drivers):

    st.subheader("📊 Simulation")

    # Initialize session state
    if "simulation_result" not in st.session_state:
        st.session_state.simulation_result = None

    if st.button(
        "🚀 Run Simulation",
        width="stretch",
    ):

        orchestrator = Orchestrator()

        result = orchestrator.run_simulation(drivers)

        # Store result
        st.session_state.simulation_result = result

        st.success("Simulation completed successfully.")

    result = st.session_state.simulation_result

    if result:

        c1, c2, c3 = st.columns(3)

        c1.metric("Volume", f"{result['Volume']:.1f}%")
        c2.metric("Shipment", f"{result['Shipment']:.1f}%")
        c3.metric("GSV", f"{result['GSV']:.1f}%")

        c4, c5, c6 = st.columns(3)

        c4.metric("NSV", f"{result['NSV']:.1f}%")
        c5.metric("Spend", f"{result['Spend']:.1f}%")
        c6.metric(
            "Fund Balance",
            f"{result['Fund Balance']:.1f}%"
        )

    return result

import streamlit as st

from agents.orchestrator import Orchestrator


def render_simulation_panel(drivers):

    st.subheader("📊 Simulation")

    if st.button(
        "🚀 Run Simulation",
        use_container_width=True,
    ):

        orchestrator = Orchestrator()

        result = orchestrator.run_simulation(drivers)

        st.success("Simulation completed successfully.")

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

    return None

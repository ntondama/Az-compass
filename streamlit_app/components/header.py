import streamlit as st


def render_header():

    st.markdown(
        """
        <div style="background:#0F62FE;
                    padding:18px;
                    border-radius:10px;
                    margin-bottom:20px;">

        <h1 style="color:white;">
        📈 Demand Copilot
        </h1>

        <p style="color:white;">
        AI Powered Retail Demand Planning
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

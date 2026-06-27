import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("Demand Copilot")

        page = st.radio(

            "Navigation",

            [

                "🏠 Dashboard",

                "📦 Product Catalog",

                "📈 Demand Simulator",

                "📑 Reports",

                "🤖 AI Copilot"

            ]

        )

    return page

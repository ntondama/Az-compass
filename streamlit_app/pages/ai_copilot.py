import streamlit as st


def show_ai_copilot():

    st.subheader("🤖 AI Copilot")

    question = st.text_area(

        "Ask a business question"

    )

    if st.button("Ask AI"):

        st.success(

            "Azure AI Foundry integration starts tomorrow."

        )

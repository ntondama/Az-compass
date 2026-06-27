import streamlit as st


def show_ai_copilot():

    st.title("🤖 AI Copilot")

    question = st.text_area(
        "Ask your business question"
    )

    if st.button("Ask AI"):

        st.success(
            "Azure AI Foundry integration starts tomorrow."
        )

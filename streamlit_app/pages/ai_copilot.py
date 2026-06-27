import streamlit as st


def show_ai_copilot():

    st.title("🤖 AI Copilot")

    question = st.text_area(
        "Ask your demand planning question"
    )

    if st.button("Ask AI"):

        st.info(
            "Agent integration will be implemented tomorrow."
        )

import streamlit as st


def show_ai_copilot():

    st.title("🤖 AI Copilot")
    st.caption("AI Assistant for Demand Planning")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask about demand planning..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        answer = """
This is a placeholder AI response.

Tomorrow we will integrate:

• Azure AI Foundry

• Orchestrator Agent

• Demand Forecast Agent

• CSV Tool

• Product Master Tool

• RAG Knowledge Base
"""

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        with st.chat_message("assistant"):

            st.markdown(answer)

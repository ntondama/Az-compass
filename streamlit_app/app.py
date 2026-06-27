import streamlit as st

st.set_page_config(
    page_title="Demand Planning Copilot",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Demand Planning Copilot")

st.write("Welcome to the Demand Planning Copilot POC.")

prompt = st.chat_input("Ask me something...")

if prompt:
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write(
        "🚀 Azure AI Foundry integration coming in the next sprint."
    )

import streamlit as st


def render_header():

    st.markdown("""
    <style>

    .main-header{
        background:linear-gradient(90deg,#0F62FE,#4589FF);
        padding:22px;
        border-radius:12px;
        margin-bottom:20px;
        box-shadow:0px 2px 10px rgba(0,0,0,.15);
    }

    .main-title{
        color:white;
        font-size:34px;
        font-weight:700;
        margin:0;
    }

    .main-subtitle{
        color:#E8F1FF;
        font-size:16px;
        margin-top:8px;
    }

    </style>

    <div class="main-header">

    <div class="main-title">
    📈 Demand Copilot
    </div>

    <div class="main-subtitle">
    AI Powered Demand Planning Platform
    </div>

    </div>
    """, unsafe_allow_html=True)

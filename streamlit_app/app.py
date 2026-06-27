import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar

from pages.dashboard import show_dashboard
from pages.product_master import show_product_master
from pages.demand_planning import show_demand_planning
from pages.reports import show_reports
from pages.ai_copilot import show_ai_copilot

st.set_page_config(
    page_title="Demand Copilot",
    page_icon="📈",
    layout="wide"
)

render_header()

page = render_sidebar()

if page == "Dashboard":
    show_dashboard()

elif page == "Product Catalog":
    show_product_master()

elif page == "Demand Simulator":
    show_demand_planning()

elif page == "Reports":
    show_reports()

elif page == "AI Copilot":
    show_ai_copilot()

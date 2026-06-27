import sys
from pathlib import Path

import streamlit as st

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from components.header import render_header
from components.sidebar import render_sidebar

from views.dashboard import show_dashboard
from views.product_catalog import show_product_catalog
from views.demand_simulator import show_demand_simulator
from views.reports import show_reports
from views.ai_copilot import show_ai_copilot


st.set_page_config(
    page_title="Demand Copilot",
    page_icon="📈",
    layout="wide",
)

render_header()

page = render_sidebar()

if page == "Dashboard":
    show_dashboard()

elif page == "Product Catalog":
    show_product_catalog()

elif page == "Demand Simulator":
    show_demand_simulator()

elif page == "Reports":
    show_reports()

elif page == "AI Copilot":
    show_ai_copilot()

import sys
from pathlib import Path

import streamlit as st

# ---------------------------------------------------
# Add project root to Python path
# ---------------------------------------------------
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# ---------------------------------------------------
# Components
# ---------------------------------------------------
from components.header import render_header
from components.sidebar import render_sidebar

# ---------------------------------------------------
# Views
# ---------------------------------------------------
from views.dashboard import show_dashboard
from views.planning_workspace import show_planning_workspace
from views.product_catalog import show_product_catalog
from views.reports import show_reports
from views.ai_copilot import show_ai_copilot

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Demand Copilot",
    page_icon="📈",
    layout="wide",
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
render_header()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
page = render_sidebar()

# ---------------------------------------------------
# Routing
# ---------------------------------------------------
if page == "🏠 Dashboard":
    show_dashboard()

elif page == "📈 Planning Workspace":
    show_planning_workspace()

elif page == "📦 Product Catalog":
    show_product_catalog()

elif page == "📊 Reports":
    show_reports()

elif page == "🤖 AI Copilot":
    show_ai_copilot()

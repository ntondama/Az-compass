import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from components.header import render_header
from components.sidebar import render_sidebar

from pages.dashboard import show_dashboard
from pages.product_catalog import show_product_catalog
from pages.demand_simulator import show_demand_simulator
from pages.reports import show_reports
from pages.ai_copilot import show_ai_copilot


def main():

    render_header()

    page = render_sidebar()

    if page == "🏠 Dashboard":

        show_dashboard()

    elif page == "📦 Product Catalog":

        show_product_catalog()

    elif page == "📈 Demand Simulator":

        show_demand_simulator()

    elif page == "📑 Reports":

        show_reports()

    elif page == "🤖 AI Copilot":

        show_ai_copilot()


if __name__ == "__main__":

    main()

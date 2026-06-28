from agents.product_agent import ProductAgent
from agents.demand_agent import DemandAgent


class Orchestrator:
    """
    Routes user requests to the appropriate agent.
    """

    def __init__(self):
        self.product_agent = ProductAgent()
        self.demand_agent = DemandAgent()

    # ---------------------------------------------------
    # Product Requests
    # ---------------------------------------------------

    def process(self, query: str):

        query = query.lower()

        if any(
            keyword in query
            for keyword in [
                "product",
                "dairy",
                "bakery",
                "grocery",
                "beverages",
                "snacks",
                "personal care",
                "home care",
                "active",
            ]
        ):
            return self.product_agent.process(query)

        return "I couldn't determine which agent should handle your request."

    # ---------------------------------------------------
    # Demand Simulation
    # ---------------------------------------------------

    def run_simulation(self, drivers: dict):

        return self.demand_agent.simulate(drivers)

from agents.product_agent import ProductAgent


class Orchestrator:

    def __init__(self):
        self.product_agent = ProductAgent()

    def process(self, query: str):

        query = query.lower()

        # Product-related requests
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

        return (
            "I couldn't determine which agent should handle your request."
        )

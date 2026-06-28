class DemandAgent:

    def __init__(self):
        pass

    def simulate(self, drivers: dict):

        result = {
            "Volume": 0,
            "Shipment": 0,
            "GSV": 0,
            "NSV": 0,
            "Spend": 0,
            "Fund Balance": 0,
            "CMA": 0
        }

        trend = drivers.get("trend", 0)
        distribution = drivers.get("distribution", 0)
        pricing = drivers.get("pricing", 0)
        trade_spend = drivers.get("trade_spend", 0)
        inventory = drivers.get("inventory", 0)

        # Trend

        result["Volume"] += trend * 2
        result["Shipment"] += trend * 2
        result["GSV"] += trend * 1.5
        result["NSV"] += trend * 1
        result["Spend"] += trend * 0.5
        result["Fund Balance"] -= trend * 0.5

        # Distribution

        result["Volume"] += distribution * 0.6
        result["Shipment"] += distribution * 0.5
        result["GSV"] += distribution * 0.3
        result["NSV"] += distribution * 0.2
        result["Spend"] += distribution * 0.2
        result["Fund Balance"] -= distribution * 0.2

        # Pricing

        result["GSV"] += pricing * 2
        result["NSV"] += pricing * 1.5
        result["Volume"] -= pricing * 0.5
        result["Shipment"] -= pricing * 0.4

        # Trade Spend

        result["Spend"] += trade_spend
        result["Volume"] += trade_spend * 0.7
        result["Shipment"] += trade_spend * 0.6
        result["Fund Balance"] -= trade_spend

        # Inventory

        result["Shipment"] += inventory * 0.8
        result["Volume"] += inventory * 0.3
        result["GSV"] += inventory * 0.2

        return result

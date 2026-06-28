from agents.demand_agent import DemandAgent

agent = DemandAgent()

response = agent.simulate({

    "trend": 2,
    "distribution": -10,
    "pricing": 1,
    "trade_spend": 3,
    "inventory": 5

})

print("\nSimulation Result\n")

for key, value in response.items():
    print(f"{key:15}: {round(value,2)}")

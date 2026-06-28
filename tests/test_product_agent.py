from agents.product_agent import ProductAgent

agent = ProductAgent()

print("\n-------------")

print(agent.process("show all products"))

print("\n-------------")

print(agent.process("show dairy products"))

print("\n-------------")

print(agent.process("show active products"))

print("\n-------------")

print(agent.process("product P1005"))

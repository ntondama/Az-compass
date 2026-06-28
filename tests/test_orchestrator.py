from agents.orchestrator import Orchestrator

orchestrator = Orchestrator()

print("\n===== Query 1 =====")
print(orchestrator.process("Show Dairy products"))

print("\n===== Query 2 =====")
print(orchestrator.process("Product P1005"))

print("\n===== Query 3 =====")
print(orchestrator.process("Show active products"))

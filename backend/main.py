from fastapi import FastAPI

app = FastAPI(title="Demand Planning Copilot")

@app.get("/")
def health():
    return {
        "status": "Running",
        "application": "Demand Planning Copilot"
    }

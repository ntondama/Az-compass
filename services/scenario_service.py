import pandas as pd
from pathlib import Path


class ScenarioService:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent

        self.file = self.project_root / "data" / "scenarios.csv"

        if not self.file.exists():

            df = pd.DataFrame(
                columns=[
                    "Scenario",
                    "Category",
                    "Volume",
                    "Shipment",
                    "GSV",
                    "NSV",
                    "Spend",
                    "Fund Balance",
                ]
            )

            df.to_csv(self.file, index=False)

    def load(self):

        return pd.read_csv(self.file)

    def save(self, scenario):

        df = self.load()

        df = pd.concat(
            [df, pd.DataFrame([scenario])],
            ignore_index=True,
        )

        df.to_csv(self.file, index=False)

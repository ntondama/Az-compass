from dataclasses import dataclass
from datetime import datetime


@dataclass
class Scenario:

    scenario_name: str

    category: str

    product: str

    trend: float

    distribution: float

    pricing: float

    trade_spend: float

    inventory: float

    volume: float

    shipment: float

    gsv: float

    nsv: float

    spend: float

    fund_balance: float

    created_time: datetime

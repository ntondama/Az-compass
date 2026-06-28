from services.simulation_service import SimulationService


class DemandAgent:
    """
    Demand Agent

    Responsible for handling demand simulation requests.
    Business calculations are delegated to SimulationService.
    """

    def __init__(self):
        self.simulation_service = SimulationService()

    def simulate(self, drivers: dict):
        """
        Execute demand simulation.

        Parameters:
            drivers (dict): Demand planning drivers.

        Returns:
            dict: Calculated business KPIs.
        """
        return self.simulation_service.calculate(drivers)

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agents.inventory_agent import InventoryAgent
from agents.order_processing_agent import OrderProcessingAgent
from agents.transport_agent import TransportAgent
from agents.maintenance_agent import MaintenanceAgent

class WarehouseModel(Model):
    """A model with agents for managing a warehouse."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, True)
        self.datacollector = DataCollector(
            agent_reporters={"InventoryAgent": lambda a: a.inventory}
        )

        # Create and add agents
        self.inventory_agent = InventoryAgent(1, self)
        self.schedule.add(self.inventory_agent)
        
        self.order_processing_agent = OrderProcessingAgent(2, self)
        self.schedule.add(self.order_processing_agent)
        
        self.transport_agent = TransportAgent(3, self)
        self.schedule.add(self.transport_agent)
        
        self.maintenance_agent = MaintenanceAgent(4, self)
        self.schedule.add(self.maintenance_agent)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

from mesa import Agent

class OrderProcessingAgent(Agent):
    """ An agent responsible for processing orders """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def process_order(self, item, quantity):
        """ Process an order by interacting with the InventoryAgent """
        inventory_agent = self.model.inventory_agent
        
        # Check if the item is in the inventory
        if item not in inventory_agent.inventory:
            return False, f"Item {item} not found in inventory."

        available_quantity = inventory_agent.check_inventory(item)
        
        if available_quantity >= quantity:
            inventory_agent.update_inventory(item, quantity)
            transport_message = self.model.transport_agent.transport_item(item, quantity)
            return True, transport_message
        else:
            return False, "Insufficient inventory."

from mesa import Agent

class InventoryAgent(Agent):
    """ An agent with inventory management capabilities """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.inventory = {"item_A": 100, "item_B": 200}

    def check_inventory(self, item):
        """ Check the inventory for the specified item """
        return self.inventory.get(item, 0)

    def update_inventory(self, item, quantity):
        """ Update the inventory for the specified item """
        if item in self.inventory:
            self.inventory[item] -= quantity
        else:
            print(f"Item {item} not found in inventory.")

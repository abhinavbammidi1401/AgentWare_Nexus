from mesa import Agent

class TransportAgent(Agent):
    """ An agent responsible for transporting items """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def transport_item(self, item, quantity):
        """ Simulate the transportation of items and return a message """
        message = f"Transporting {quantity} of {item} to dispatch area."
        print(message)  # Optional: for debugging
        return message

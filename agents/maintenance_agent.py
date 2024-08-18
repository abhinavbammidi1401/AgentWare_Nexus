from mesa import Agent

class MaintenanceAgent(Agent):
    """ An agent responsible for maintaining the environment """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def monitor_environment(self):
        """ Simulate environment monitoring and return a message """
        # Simulate some monitoring process
        return "Monitoring complete. Environment is stable."

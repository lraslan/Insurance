import uuid
import random

# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID= str(uuid.uuid1())
        self.name = name
        self.address = address
        self.customers = []

    def assignCustomer(self, customer):
        self.customers.append(customer)
        return customer

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name, 
            'address': self.address,
            'customers': self.customers,
        }

    def transfer(self, agent_id):
        agent = random.choices(self.agents, k=1)
        if (agent_id not in agent):
            for customers in agent:
                agent.append()
            return agent
from Customer import *
from Agent import *
from Claim import *
from PaymentIn import *

class InsuranceCompany:
    def __init__(self, name):
        self.name = name # Name of the Insurance company
        self.customers = [] # list of customers
        self.agents = []  # list of dealers
        self.claims = [] # list of claims
        self.payments = []  # list of payments

    def getCustomers(self):
        return list(self.customers)

    def addCustomer(self, name, address):
        c = Customer(name, address)
        self.customers.append(c)
        print(c.ID)
        return c.ID
    
    def getCustomerById(self, id_):
        for d in self.customers:
            if(d.ID==id_):
                return d
        return None

    def deleteCustomer (self, customer_id):
        c = self.getCustomerById(customer_id)
        self.customers.remove(c)


    def getAgents(self):
        return list(self.agents)

    def addAgent(self, name, address):
        a = Agent(name, address)
        self.agents.append(a)
        print(a.ID)
        return a.ID

    def getAgentById(self, id_):
        for d in self.agents:
            if(d.ID==id_):
                return d
        return None

# There is a silly mistake happening here but i gave up on finding it
    def transfer(self, agent_id):
        agent = random.choices(self.agents, k=1)
        a = self.getAgentById(agent_id)
        if (agent_id not in agent):
            # try adding a loop to check each customer in customers
            cs = self.addCustomer(a.customers)
            agent.append(cs)
            return agent

    def deleteAgent (self, agent_id):
        self.transfer(agent_id)
        a = self.getAgentById(agent_id)
        self.agents.remove(a)

    def getClaims (self):
        return list(self.claims)

    def addClaim (self, customer, date, incident_description, claim_amount):
        a = Claim(customer, date, incident_description, claim_amount)
        self.claims.append(a)
        print(a.ID)
        return a.ID

    def getClaimById(self, id_):
        for d in self.claims:
            if(d.ID==id_):
                return d
        return None

    def getPayments(self):
        return list(self.payments)

    def addPayment(self, payment):
        self.payments.append(payment)
        return payment

    def addPaymentIn(self, date, customer_id, amount_received):
        inPay = PaymentIn(date, customer_id, amount_received)
        self.payments.append(inPay)
        print(inPay.ID)
        return inPay.ID

    def getPaymentById(self, id_):
        for d in self.payments:
            if(d.ID==id_):
                return d
        return None

    def addPaymentOut(self, date, agent_id, amount_sent):
        outPay = PaymentOut(date, agent_id, amount_sent)
        self.payments.append(outPay)
        print(outPay.ID)
        return outPay.ID




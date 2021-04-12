from Customer import *

import uuid

# Represents the insurance claims
class Claim:
    def __init__(self, customer, date, incident_description, claim_amount):
        self.ID = str(uuid.uuid1())
        self.customer = customer
        self.date = date
        self.incident_description = incident_description
        self.claim_amount = claim_amount
        self.status = ""

    def getCustomerID(self, customer):
        self.customer = customer.ID
        return customer.ID

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'customer': self.customer,
            'date': self.date,
            'incident_description': self.incident_description, 
            'claim_amount': self.claim_amount,
            'status': self.status,
        }

    def changeStatus(self, approved_amount):
        status = ["FULLY COVERED", "REJECTED", "PARTLY COVERED"]
        if (approved_amount == 100):
            self.status = status[0]
            return status[0]
        if (approved_amount == 0):
            self.status = status[1]
            return status[1]
        if (approved_amount < 100):
            self.status = status[2]
            return status[2]

    # the approved_amount represent the percentage that will cover the claim amount
    # extra function no useful usage for it now
    def getInfo(self, approved_amount):
        ca = self.claim_amount
        if (approved_amount == 100):
            ca = ca - ca*(approved_amount/100)
            return ca
        if (approved_amount == 0):
            ca = ca - ca*(approved_amount/100)
            return ca
        if (approved_amount < 100):
            ca = ca - ca*(approved_amount/100)
            return ca

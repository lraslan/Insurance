from flask import Flask, request, jsonify
from InsuranceCompany import *
from Customer import *
from Agent import *
from Claim import *

app = Flask(__name__)

# Root object for the insurance company
company = InsuranceCompany ("Be-Safe Insurance Company")

#Add a new customer (parameters: name, address).
@app.route("/customer", methods=["POST"])
def addCustomer():
    # parameters are passed in the body of the request
    cid = company.addCustomer(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new customer with ID {cid}")

#Return the details of a customer of the given customer_id.
@app.route("/customer/<customer_id>", methods=["GET"])
def customerInfo(customer_id):
    c = company.getCustomerById(customer_id)
    if(c!=None):
        return jsonify(c.serialize())
    return jsonify(
            success = False, 
            message = "Customer not found")

#Add a new car (parameters: model, numberplate).
@app.route("/customer/<customer_id>/car", methods=["POST"])
def addCar(customer_id):
    c = company.getCustomerById(customer_id)
    if(c!=None):
        car = Car(request.args.get('model'), request.args.get('number_plate'), request.args.get('motor_power'), request.args.get('year'))
        c.addCar(car.serialize())
    return jsonify(
            success = c!=None,
            message = "Customer not found")
    
@app.route("/customer/<customer_id>", methods=["DELETE"])
def deleteCustomer(customer_id):
    result = company.deleteCustomer(customer_id)
    if(result): 
        message = f"Customer with id{customer_id} was deleted"
    else: 
        message = "Customer not found"
    return jsonify(
            success = result, 
            message = message)

@app.route("/customers", methods=["GET"])
def allCustomers():
    return jsonify(customers=[h.serialize() for h in company.getCustomers()])


#Add a new agent (parameters: name, address).
@app.route("/agent", methods=["POST"])
def addAgent():
    # parameters are passed in the body of the request
    aid = company.addAgent(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new agent with ID {aid}")


#Return the details of a customer of the given customer_id.
@app.route("/agent/<agent_id>", methods=["GET"])
def agentInfo(agent_id):
    a = company.getAgentById(agent_id)
    if(a!=None):
        return jsonify(a.serialize())
    return jsonify(
            success = False, 
            message = "Agent not found")


@app.route("/agent/<agent_id>", methods=["DELETE"])
def deleteAgent(agent_id):
    result = company.deleteAgent(agent_id)
    if(result): 
        message = f"Agent with id{agent_id} was deleted"
    else: 
        message = "Agent not found"
    return jsonify(
            success = result, 
            message = message)

@app.route("/agent/<agent_id>/<customer_id>", methods=["POST"])
def assignCustomer(agent_id,customer_id):
    a = company.getAgentById(agent_id)
    c = company.getCustomerById(customer_id)
    if(c!=None):
        a.assignCustomer(c.serialize())
    return jsonify(
            success = c!=None,
            message = "Agent not found")

@app.route("/agents", methods=["GET"])
def allAgents():
    return jsonify(agents=[h.serialize() for h in company.getAgents()])


@app.route("/claims/<customer_id>/file", methods=["POST"])
def addClaim(customer_id):
    cus = company.getCustomerById(customer_id)
    if(cus!=None):
        claim = company.addClaim(customer_id, request.args.get('date'), request.args.get('incident_description'), request.args.get('claim_amount'))
        return jsonify(f"Added a new claim with ID {claim}")
    return jsonify(
            success = cus!=None,
            message = "Claims found")

#Return the details of a claim of the given claim_id.
@app.route("/claims/<claim_id>", methods=["GET"])
def claimInfo(claim_id):
    c = company.getClaimById(claim_id)
    if(c!=None):
        return jsonify(c.serialize())
    return jsonify(
            success = False,
            message = "claim not found")

@app.route("/claims/<claim_id>/status", methods=["PUT"])
def changeStatus(claim_id):
    c = company.getClaimById(claim_id)
    if (c != None):
        claimStatus = c.changeStatus(int(request.args.get('approved_amount')))
        return jsonify(f"Status got changed {claimStatus}")
        #request.args.update('status', c.changeStatus(claim))
    return jsonify(
        success=c != None,
        message="Claim not found")

@app.route("/claims", methods=["GET"])
def allClaims():
    return jsonify(claims=[h.serialize() for h in company.getClaims()])

@app.route("/payment/in/", methods=["POST"])
def addPaymentIn():
    pin = PaymentIn(request.args.get('date'), company.getCustomerById(request.args.get('customer_id')), request.args.get('amount_received'))
    pid = company.addPayment(pin.serialize())
    return jsonify(f"Added a new payment in with ID {pid}")

@app.route("/payment/out/", methods=["POST"])
def addPaymentOut():
    pout = PaymentOut(request.args.get('date'), company.getAgentById(request.args.get('agent_id')), request.args.get('amount_sent'))
    pid = company.addPayment(pout.serialize())
    return jsonify(f"Added a new payment out with ID {pid}")

@app.route("/payments/", methods=["GET"])
def allPayments():
    return jsonify(payments=[h.serialize() for h in company.getPayments()])

@app.route("/stats/claims", methods=["GET"])

@app.route("/stats/revenues", methods=["GET"])

@app.route("/stats/agents", methods=["GET"])

###DO NOT CHANGE CODE BELOW THIS LINE ##############################
@app.route("/")
def index():
    return jsonify(
            success = True, 
            message = "Your server is running! Welcome to the Insurance Company API.")

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE"
    return response

if __name__ == "__main__":
    app.run(debug=False, port=8888)

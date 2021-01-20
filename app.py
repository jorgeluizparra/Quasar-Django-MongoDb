from flask import Flask, request, Response
from flask_cors import CORS
from database.db import initialize_db
from database.models import Transaction
from functions import count_bill

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'database',
    'host': 'localhost',
    'port': 27017
}

db = initialize_db(app)

# Working test
@app.route('/')
def test():
    return '<h3>Service is running...</h3>'

# Get all stored transactions
@app.route('/transactions')
def get_transactions():
    transactions = Transaction.objects().to_json()
    return Response(transactions, mimetype="application/json", status=200)

# Save new transaction
@app.route('/transactions', methods=['POST'])
def add_transaction():
    body = request.get_json()

    rest = float(body.get("received")) - float(body.get("total"))

    if(rest < 0):
        return {"response": "The value received must be bigger than the total."}

    else:
        bills_quantities = count_bill(rest)

        transaction = Transaction(
            client_cpf = str(body.get("client_cpf")),
            total = float(body.get("total")),
            received = float(body.get("received")),
            change = rest,
            bills_quantities = bills_quantities
        ).save()

        return Response(transaction.to_json(), mimetype="application/json", status=200)

# Get a transaction
@app.route('/transactions/<id>')
def get_transaction(id):
    transaction = Transaction.objects.get(id=id).to_json()
    return Response(transaction, mimetype="application/json", status=200)

# Get a transaction by client CPF
@app.route('/transactions/query')
def get_transactions_by_cpf():
    cpf = request.args['cpf']
    transaction = Transaction.objects.filter(client_cpf=cpf).to_json()
    return Response(transaction, mimetype="application/json", status=200)

# Update the transaction infromation
@app.route('/transactions/<id>', methods=['PUT'])
def update_transaction(id):
    body = request.get_json()

    rest = float(body.get("received")) - float(body.get("total"))

    if(rest < 0):
        return {"response": "The value received must be bigger than the total."}

    else:
        bills_quantities = count_bill(rest)

        save = Transaction.objects.get(id=id).update(
            client_cpf = str(body.get("client_cpf")),
            total = float(body.get("total")),
            received = float(body.get("received")),
            change = rest,
            bills_quantities = bills_quantities
        )

        if(save):
            transaction = Transaction.objects.get(id=id).to_json()
            return Response( transaction, mimetype="application/json", status=200)

        else:
            return Response( save, mimetype="application/json", status=200)

# Delete a transaction
@app.route('/transactions/<id>', methods=['DELETE'])
def delete_transaction(id):
    Transaction.objects.get(id=id).delete()
    return 'Deleted', 200

if __name__ == "__main__":
    app.run(debug=True)

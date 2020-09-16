# Read-me

## Requirements
MongoDB installed in the local machine

## Run app
pipenv shell
py app.py

## APIs
### GET -> http://127.0.0.1:5000/transactions
Get all the transactions

### POST -> http://127.0.0.1:5000/transactions
Save a new transactions
#### Body
{
    "client_cpf": "40174942850",
    "total": 488.25,
    "received": 500.00
}

### GET -> http://127.0.0.1:5000/transactions/<id>
Get one transaction

### PUT -> http://127.0.0.1:5000/transactions/<id>
Update the transaction
#### Body
{
    "client_cpf": "40174942850",
    "total": 488.25,
    "received": 500.00
}

### DELETE -> http://127.0.0.1:5000/transactions/<id>
Delete the transaction
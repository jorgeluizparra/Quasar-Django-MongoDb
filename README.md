# EasyCounter

## Requirements
1. MongoDB, python, pip, pipenv installed in the local machine

### To install `pip` run the command
`python -m pip install -U pip`

### To install `pipenv` run the command
`pip install pipenv`

## Run app
Install the dependencies
`pipenv install`

Open the shell
`pipenv shell`

Run the app
`py app.py`

## APIs
### GET -> http://127.0.0.1:5000/transactions
Get all the transactions

### POST -> http://127.0.0.1:5000/transactions
Save a new transactions
#### Body
`{
    "client_cpf": "40174942850",
    "total": 488.25,
    "received": 500.00
}`

### GET -> http://127.0.0.1:5000/transactions/<id>
Get one transaction
  
### GET -> http://127.0.0.1:5000/transactions/query?cpf=<cpf>
Get the transactions by the Client CPF

### PUT -> http://127.0.0.1:5000/transactions/<id>
Update the transaction
    
#### Body
`{
    "client_cpf": "40174942850",
    "total": 488.25,
    "received": 500.00
}`

### DELETE -> http://127.0.0.1:5000/transactions/<id>
Delete the transaction

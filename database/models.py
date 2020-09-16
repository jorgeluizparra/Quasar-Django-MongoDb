from .db import db
import mongoengine_goodjson as gj

class Transaction(gj.Document):
    client_cpf = db.StringField(min_value=10, max_value=12, required=True)
    total = db.FloatField(min_value=None, max_value=None, required=True)
    received = db.FloatField(min_value=None, max_value=None, required=True)
    change = db.FloatField(min_value=None, max_value=None, required=True)
    bills_quantities = db.ListField(db.DictField(), required=True)
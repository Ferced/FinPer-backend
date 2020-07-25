
from .. import db

class CreditCardDetails(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "credit_cards_details"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id= db.Column(db.Integer)
    credit_card_bank_name= db.Column(db.String(50))
    credit_last_four_numbers= db.Column(db.Integer)
    credit_card_network_bank= db.Column(db.String(50))
    custom_name= db.Column(db.String(100))
    registered_on = db.Column(db.DateTime, nullable=False)

class CreditCardExpenses(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "credit_cards_expenses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    credit_card_id = db.Column(db.Integer)
    amount_of_payments=db.Column(db.Integer)
    number_of_next_payment=db.Column(db.Integer)
    price_of_expenditure=db.Column(db.Integer)
    name_of_expenditure=db.Column(db.String(50))
    currency_iso_code=db.Column(db.String(10))
    continue_payment=db.Column(db.Boolean)
    registered_on = db.Column(db.DateTime, nullable=False)

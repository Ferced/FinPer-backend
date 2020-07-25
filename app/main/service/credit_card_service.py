import uuid
import datetime
from flask import jsonify
from app.main import db
from app.main.model.credit_card import CreditCardDetails,CreditCardExpenses
from ..service.user_service import get_a_user_by_email


def save_new_credit_card(data):
    #list_of_credit_cards = CreditCardDetails.query.filter_by(email=data['user_id'])
    #print (list_of_credit_cards)
    #if not list_of_credit_cards:
    if True:    
        new_credit_card = CreditCardDetails(
            user_id= get_a_user_by_email(data['email']),
            credit_card_bank_name= data['credit_card_bank_name'],
            credit_last_four_numbers= data['credit_last_four_numbers'],
            credit_card_network_bank= data['credit_card_network_bank'],
            custom_name= data['custom_name'],
            registered_on=datetime.datetime.utcnow()
        )

        save_changes(new_credit_card)

        response_object = {
            'status': 'success',
            'message': 'Successfully added the credit card.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Credit card already exists.',
        }
        return response_object, 409


def get_all_credit_cards_by_user(data):
    user_id_=get_a_user_by_email(data['email'])
    lista = CreditCardDetails.query.filter_by(user_id=user_id_).all()
    return lista

def get_all_credit_cards():
    return CreditCardDetails.query.all()

def get_credit_card_by_user(data):
    credit_card_details= CreditCardDetails.query.filter_by(credit_card_bank_name= data['credit_card_bank_name'],credit_last_four_numbers= data['credit_last_four_numbers'],credit_card_network_bank= data['credit_card_network_bank'],custom_name= data['custom_name']).first()
    
    return credit_card_details.id


def save_new_expenditure(data):
    #list_of_credit_cards = CreditCardDetails.query.filter_by(email=data['user_id'])
    #print (list_of_credit_cards)
    #if not list_of_credit_cards:

    print (
        get_all_expenses_by_user(data)
    )

    if True:    
        new_expenditure = CreditCardExpenses(
            credit_card_id=get_credit_card_by_user(data),
            amount_of_payments=data['amount_of_payments'],
            number_of_next_payment=data['number_of_next_payment'],
            price_of_expenditure=data['price_of_expenditure'],
            name_of_expenditure=data['name_of_expenditure'],
            currency_iso_code=data['currency_iso_code'],
            continue_payment=data['continue_payment'],
            registered_on=datetime.datetime.utcnow()
        )

        print ("-------------------------------------- \nLLEGO HASTA ACA \n --------------------------------------")
        save_changes(new_expenditure)

        response_object = {
            'status': 'success',
            'message': 'Successfully added the expenditure.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'The expenditure already exists.',
        }
        return response_object, 409 





def get_all_expenses_by_user(data):
    credit_card_id = get_credit_card_by_user(data)
    return CreditCardExpenses.query.filter_by(credit_card_id=credit_card_id).all()

def get_all_expenses():
    CreditCardExpenses.query.all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()


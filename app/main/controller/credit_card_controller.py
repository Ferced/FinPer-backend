from flask import request
from flask_restplus import Resource

from app.main.util.decorator import user_credentials_required
from ..util.dto import CreditCardDto
from ..service.credit_card_service import  save_new_expenditure,get_all_expenses_by_user,get_all_credit_cards_by_user,save_new_credit_card

api = CreditCardDto.api

credit_card_details = CreditCardDto.credit_card_details
credit_card_expenses = CreditCardDto.credit_card_expenses


@api.route('/details/')
class CreditCardDetails(Resource):
    #@user_credentials_required
    @api.marshal_list_with(credit_card_details, envelope='data')
    def get(self):
        """List all credit card from x user"""
        data = request.json
        return get_all_credit_cards_by_user(data)
    @api.expect(credit_card_details, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new credit card """
        data = request.json
        return save_new_credit_card(data)


@api.route('/expenses/')
class CreditCardExpenses(Resource):
     #@user_credentials_required
    @api.marshal_list_with(credit_card_expenses, envelope='data')
    def get(self):
        """List all expenses from x credit card"""
        data = request.json
        return get_all_expenses_by_user(data)
    @api.expect(credit_card_expenses, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new credit card """
        data = request.json
        return save_new_expenditure(data)



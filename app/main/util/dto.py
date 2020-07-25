from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class TestDto:
    api = Namespace('test', description='Just a test')
    test = api.model('test', {
        'test_message': fields.String(required=True, description='A message to send the test class'),
    })


class CreditCardDto:
    api = Namespace('credit_card', description='all actions related to credit card')
    credit_card_details = api.model('credit_card_details', {
        'user_id': fields.Integer(description='User id who owns this credit card'),
        'credit_card_bank_name': fields.String(required=True, description='Credit bank name (Galicia, HSBC, Santander, etc...)'),
        'credit_last_four_numbers': fields.Integer(required=True, description='Last four numbers of the credit card'),
        'credit_card_network_bank': fields.String(required=True, description='Credit card network (VISA, Mastercard, American Express)'),
        'custom_name': fields.String(required=True, description='Credit card last four numbers')
    })
    credit_card_expenses = api.model('credit_card_expenses', {
        'amount_of_payments': fields.Integer(required=True, description='Amount of payments of the expenditure'),
        'number_of_next_payment': fields.Integer(required=True, description='Next number of payment'),
        'price_of_expenditure': fields.Integer(required=True, description='Price of expenditure'),
        'name_of_expenditure': fields.String(required=True, description='Name of expenditure'),
        'currency_iso_code': fields.String(required=True, description='ISO code currency (USD, ARS, EUR, etc..)'),
    })

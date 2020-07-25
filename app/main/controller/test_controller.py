from flask import request
from flask_restplus import Resource

from app.main.util.decorator import user_credentials_required
from app.main.service.auth_helper import Auth
from ..util.dto import TestDto, AuthDto
api = TestDto.api
user_auth = AuthDto.user_auth

@api.route('/')
class TestController(Resource):

    @api.expect(user_auth, validate=True)
    @user_credentials_required
    def get(self):
        # get the post data
        post_data = request.json
        data,status =Auth.check_user_credentials(data=post_data)
        if (status == 200):
            return "test succesufle"
        return "test faiilud"



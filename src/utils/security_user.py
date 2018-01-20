from flasgger import swag_from
from flask_restful import  Resource
from flask import request, jsonify, json
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

class JwtIdentify(object):
    def __init__(self, id):
        self.id = id


class SecurityUser(Resource):

    @swag_from('../../spec/app/auth.yml', methods=['POST'])
    def post(self):
        pass

    @staticmethod
    def authenticate(username, password):
        user = {}
        user['id'] = 1
        user['name'] = 'user1'
        user['vid'] = 'DFF_TECH'
        return JwtIdentify(user)

    @staticmethod
    def identity(payload):
        jwt_identity = payload['identity']
        return jwt_identity

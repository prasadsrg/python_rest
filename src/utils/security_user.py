from flasgger import swag_from
from flask_restful import  Resource
from flask import request, jsonify, json

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


class SecurityUser(Resource):

    @swag_from('../../spec/app/auth.yml', methods=['POST'])
    def post(self):
        pass

    @staticmethod
    def authenticate(username, password):
        user = {}
        user['id'] = (1, 'user1', 'abcxyz'),
        user['password'] = password
        print(user)
        return User(1, 'user1', 'abcxyz')

    @staticmethod
    def identity(payload):
        user = payload['identity']
        print(user)
        return user
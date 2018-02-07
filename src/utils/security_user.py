from flasgger import swag_from
from flask_restful import  Resource
from flask import request, jsonify, json
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from db import db
from sqlalchemy import text

class JwtIdentify(object):
    def __init__(self, id):
        self.id = id


class SecurityUser(Resource):

    @swag_from('../../spec/app/auth.yml', methods=['POST'])
    def post(self):
        print("inside post")
        pass

    @staticmethod
    def authenticate(username, password):
        param = {}
        param["vid"] = username.split('-')[0]
        param["userid"] = username.split('-')[1]
        param["password"] = password
        print(param)
        sql = """
            select
                id,
                name,
                email,
                mobile,
                role,
                branch_id,
                vid
            from profile 
            where vid = '{vid}'
            and (email = '{userid}' or mobile = '{userid}')
            and password = '{password}'
        """.format(**param)
        print(sql)
        print("inside authenticate")
        result = db.engine.execute(text(sql)).first();
        print(result)
        user = {}
        user['id'] = result[0]
        user['name'] = result[1]
        user['email'] = result[2]
        user['mobile'] = result[3]
        user['role'] = result[4]
        user['branchId'] = result[5]
        user['vid'] = result[6]
        # user['id'] = 'SUPPORT_DFF_USER'
        # user['name'] = 'Support User'
        # user['email'] = 'support@dfftech.com'
        # user['mobile'] = '123456789'
        # user['role'] = 'SuperAdmin'
        # user['vid'] = 'DFF'
        print(user)
        return JwtIdentify(user)

    @staticmethod
    def identity(payload):
        jwt_identity = payload['identity']
        return jwt_identity

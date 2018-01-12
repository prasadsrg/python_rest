from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT
from flasgger import Swagger

app = Flask(__name__)
app.secret_key = 'abcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

from utils.security_user import SecurityUser

JWT.JWT_EXPIRATION_DELTA = 9999
jwt = JWT(app, SecurityUser.authenticate, SecurityUser.identity)

from resources.user_resource import UserResource
#
#
# class UserResource(Resource):
#
#
#     def get(self):
#         # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
#         # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
#         return {'status': 1, 'data': 'HelloWorld'}
#
#
#     def post(self):
#         # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
#         # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
#         return {'status': 1, 'data': 'HelloWorld'}

api.add_resource(UserResource, '/user')
api.add_resource(SecurityUser, '/auth')

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
#     response.headers.add('Access-Control-Expose-Headers', "Authorization")
#     response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
#     response.headers.add('Access-Control-Allow-Credentials', "true")
#     response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
#     return response

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    # header = request.headers.get('Authorization')
    # if header:
    #     _, token = header.split()
    #     request.identity = SecurityUser.identity(jwt.jwt_decode_callback(token))
    #     print(request.identity)
    return response

if __name__ == '__main__':
    app.config['SWAGGER'] = {
        "swagger_version": "2.0",
        "title": "ABCD",
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
    }
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "version": "1.0",
        },
        "consumes": [
            "application/json",
            "application/x-www-form-urlencoded",
        ],
        "produces": [
            "application/json",
        ],
        "securityDefinitions": {
            "jwt": {
                "type": 'apiKey',
                "name": 'Authorization',
                "in": 'header'
            }
        },
        "security": [
            {"jwt": []}
        ]
    },)
    from db import db
    db.init_app(app)
    app.run(port=5001, debug=True)
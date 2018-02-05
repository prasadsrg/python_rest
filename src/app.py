from flasgger import Swagger
from flask import Flask, request
from flask_jwt import JWT
from flask_restful import Api
from config import app_config
import os
import datetime

config_name = os.getenv('ENV', 'dev')
app = Flask(__name__, instance_relative_config=False)
print(config_name)
api = Api(app)
app.config.from_object(app_config[config_name])
#app.config.from_pyfile('config.py')

print(app.config)

from utils.security_user import SecurityUser

JWT.JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=9999999)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=9999999)
jwt = JWT(app, SecurityUser.authenticate, SecurityUser.identity)
api.add_resource(SecurityUser, '/auth')
from resources.user_resource import UserResource
api.add_resource(UserResource, '/user')

from resources.vendor_resource import VendorResource
api.add_resource(VendorResource, '/vendor')

from resources.branch_resource import BranchResource
api.add_resource(BranchResource, '/branch')

from resources.consumer_resource import ConsumerResource
api.add_resource(ConsumerResource, '/consumer')

from resources.apex_report_data_resource import ApexReportDataResource
api.add_resource(ApexReportDataResource, '/apex_report_data')
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
    app.run(host='0.0.0.0', port=5001, debug=True)
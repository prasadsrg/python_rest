from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)
app.secret_key = 'abcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#jwt = JWT(app, authenticate, identity)
# api.add_resource(UserResource, '/user/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5001, debug=True)
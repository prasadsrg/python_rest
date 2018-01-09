from flask_restful import  Resource
from flask_jwt import jwt_required

class UserResource(Resource):

    def post(self):
        # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
        # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
        None
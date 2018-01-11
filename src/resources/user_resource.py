from flask import request, jsonify, json
from flask_restful import  Resource
from flask_jwt import jwt_required, current_identity
from flasgger import swag_from


class UserResource (Resource):

    @jwt_required()
    @swag_from('../../spec/user/save.yml')
    def put(self):
        req_json = json.loads(request.data)
        req_data = req_json.get('data', None)

        res_json = { }
        res_json['status']=1
        res_json['data'] = req_data
        print(current_identity)
        return jsonify(res_json)

    @swag_from('../../spec/user/search.yml')
    def post(self):
        # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
        # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
        return {'status': 1, 'data': 'HelloWorld'}

    @swag_from('../../spec/user/entity.yml')
    def get(self):
        id = request.args['id']
        res_json = { }
        res_json['status']=1
        res_json['data'] = {}
        res_data =  res_json['data']
        res_data['id']=id
        return jsonify(res_json)

    @swag_from('../../spec/user/delete.yml')
    def delete(self):
        # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
        # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
        return {'status': 1, 'data': 'HelloWorld'}

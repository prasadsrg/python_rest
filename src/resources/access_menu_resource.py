from flask import request, jsonify, json
from flask_restful import  Resource
from flask_jwt import jwt_required, current_identity
from flasgger import swag_from

from services.access_menu_service import AccessMenuService
from utils.util import model_to_dict

class AccessMenuResource(Resource):

    access_menu_service = AccessMenuService()

    @jwt_required()

    @swag_from('../../spec/access_menu/search.yml')
    def post(self):
        try :
            res_data = self.access_menu_service.search()
            print(res_data)
            res_json = {'status': 1, 'data': [model_to_dict(x) for x in res_data]}
            print(res_json)
        except Exception as e:
            print(e)
            if e.args:
                res_data = e.args[0]
            else:
                res_data = e
            res_json = {'status': 0, 'data': res_data}
        return jsonify(res_json)

    @swag_from('../../spec/access_menu/entity.yml')
    def get(self):
        id = request.args['id']
        res_json = { }
        res_json['status']=1
        res_json['data'] = {}
        res_data =  res_json['data']
        res_data['id']=id
        return jsonify(res_json)



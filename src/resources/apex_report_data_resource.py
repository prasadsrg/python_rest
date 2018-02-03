from flask import request, jsonify, json
from flask_restful import  Resource
from flask_jwt import jwt_required, current_identity
from flasgger import swag_from

from services.apex_report_data_service import ApexReportDataService
from utils.util import model_to_dict

class ApexReportDataResource (Resource):

    apex_report_data_service = ApexReportDataService()

    @jwt_required()
    @swag_from('../../spec/apex_report_data/save.yml')
    def put(self):
        try :
            self.apex_report_data_service.session_info = current_identity
            req_json = json.loads(request.data)
            req_data = req_json.get('data', None)
            res_data = self.apex_report_data_service.save(req_data)
            res_json = {'status': 1, 'data': res_data}
        except Exception as e:
            if e.args:
                res_data = e.args[0]
            else:
                res_data = e
            res_json = {'status': 0, 'data': res_data}
        return jsonify(res_json)


    @swag_from('../../spec/apex_report_data/search.yml')
    def post(self):
        try:
            res_data = self.apex_report_data_service.search()
            print(res_data)
            res_json = {'status': 1, 'data': [ model_to_dict(x) for x in res_data ]}
            print(res_json)
        except Exception as e:
            print(e)
            if e.args:
                res_data = e.args[0]
            else:
                res_data = e
            res_json = {'status': 0, 'data': res_data}
        return jsonify(res_json)

    @swag_from('../../spec/apex_report_data/entity.yml')
    def get(self):
        id = request.args['id']
        res_json = { }
        res_json['status']=1
        res_json['data'] = {}
        res_data =  res_json['data']
        res_data['id']=id
        return jsonify(res_json)

    @jwt_required()
    @swag_from('../../spec/apex_report_data/delete.yml')
    def delete(self):
        # return { 'status': 1, data : list(map( lambda x: x.json(), ItemModel.query.all() ) ) }
        # return { 'status': 1, data : [x.json for x in ItemModel.query.all() ] }
        return {'status': 1, 'data': 'HelloWorld'}

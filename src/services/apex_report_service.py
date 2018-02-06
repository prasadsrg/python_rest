from db import db
import json
from models.apex_report_model import ApexReportModel
from mappers.apex_report_mapper import ApexReportMapper

class ApexReportService:

    session_info = None

    def save(self, req_data):
        vendor = None
        if req_data.get('id', None) is not None:
           vendor = ApexReportModel.query.filter_by(id=req_data.get('id')).first()
        if vendor is None:
            vendor = ApexReportModel()

        ApexReportMapper(vendor, req_data).model_mapping()
        db.session.add(vendor)
        db.session.commit()
        return {'message': 'Saved Successfully'}


    def search(self):
        data_list = ApexReportModel.query.all()
        print(data_list)
        return data_list
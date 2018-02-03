from db import db
from utils.util import uid
from models.apex_report_model import ApexReportModel
from mappers.apex_report_mapper import ApexReportMapper

class ApexReportService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = ApexReportModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = ApexReportModel()
            model.id = uid()

        ApexReportMapper(model, view).model_mapping()
        return model

    def save(self, req_data):
        apexReport = self.mapping(None, req_data)
        db.session.add(apexReport)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': apexReport.id}


    def search(self):
        print("apex report service")
        data_list = ApexReportModel.query.all()
        print(data_list[0].__dict__)
        return data_list
from db import db
from utils.util import uid
from models.apex_report_data_model import ApexReportDataModel
from models.apex_report_model import ApexReportModel
from mappers.apex_report_data_mapper import ApexReportDataMapper
from mappers.apex_report_mapper import ApexReportMapper
import datetime


class ApexReportDataService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = ApexReportDataModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = ApexReportDataModel()
            model.id = uid()
            model.apexReport = ApexReportModel()
            model.apexReport.id = model.id

        model.vid = self.session_info['vid']
        ApexReportDataMapper(model, view).model_mapping()
        ApexReportMapper(model.apexReport, view.get('apex_report', None)).model_mapping()
        return model

    def save(self, req_data):
        apex_report_data = self.mapping(None, req_data)
        db.session.add(apex_report_data)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': apex_report_data.id}

    def search(self):
        print("branch service")
        data_list = ApexReportDataModel.query.all()
        print(data_list[0].__dict__)
        return data_list
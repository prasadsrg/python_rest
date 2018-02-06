from db import db
from models.apex_data_model import ApexDataModel
from mappers.apex_data_mapper import ApexDataMapper
import datetime


class ApexDataService:
    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = ApexDataModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = ApexDataModel()


        model.vid = self.session_info['vid']

        ApexDataMapper(model, view).model_mapping()

        return model


    def save(self, req_data):
        apex_data = self.mapping(None, req_data)
        db.session.add(apex_data)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': apex_data.id}


    def search(self):
        data_list = ApexDataModel.query.all()
        print(data_list[0].__dict__)
        return data_list

from db import db
from models.app_data_model import AppDataModel
from mappers.app_data_mapper import AppDataMapper
import datetime

class AppDataServices:
    session_info = None

    def mapping(self, model, view):
        if view.get('id', None) is not None:
            model = AppDataModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = AppDataModel()
            model.id = uid()



        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()

        AppDataMapper(model, view).model_mapping()
        return model

    def save(self, req_data):
        app_data = self.mapping(None, req_data)
        db.session.add(app_data)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': app_data.id}

    def search(self):
        data_list = AppDataModel.query.all()
        print(data_list[0].__dict__)
        return data_list
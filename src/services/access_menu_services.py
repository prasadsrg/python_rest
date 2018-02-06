from db import db
from utils.util import uid
from models.access_menu_model import AccessMenuModel
from mappers.access_menu_mapper import AccessMenuMapper
import datetime

class AccessMenuServices:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = AccessMenuModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = AccessMenuModel()
            model.id = uid()

        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()

        AccessMenuMapper(model, view).model_mapping()

        return model

    def save(self, req_data):
        access_menu = self.mapping(None, req_data)
        db.session.add(access_menu)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': access_menu.id}

    def search(self):
        data_list = AccessMenuModel.query.all()
        print(data_list[0].__dict__)
        return data_list
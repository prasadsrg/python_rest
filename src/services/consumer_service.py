from db import db
from utils.util import uid
from models.consumer_model import ConsumerModel
from mappers.consumer_mapper import ConsumerMapper
import datetime

class ConsumerService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = ConsumerModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = ConsumerModel()
            model.id = uid()

        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()

        ConsumerMapper(model, view).model_mapping()
        return model

    def save(self, req_data):
        consumer = self.mapping(None, req_data)
        db.session.add(consumer)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': consumer.id}


    def search(self):
        print("branch service")
        data_list = ConsumerModel.query.all()
        print(data_list[0].__dict__)
        return data_list
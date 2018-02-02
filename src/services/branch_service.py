from db import db
from utils.util import uid
from models.branch_model import BranchModel
from models.address_model import AddressModel
from helpers.branch_helper import BranchHelper
from helpers.address_helper import AddressHelper
import datetime

class BranchService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = BranchModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = BranchModel()
            model.id = uid()
            model.address = AddressModel()
            model.address.id = model.id

        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()

        BranchHelper(model, view).model_mapping()
        AddressHelper(model.address, view.get('address', None)).model_mapping()
        return model

    def save(self, req_data):
        branch = self.mapping(None, req_data)
        db.session.add(branch)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': branch.id}


    def search(self):
        print("branch service")
        data_list = BranchModel.query.all()
        print(data_list[0].__dict__)
        return data_list
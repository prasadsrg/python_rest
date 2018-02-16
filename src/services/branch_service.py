from db import db
from utils.util import uid
from models.branch_model import BranchModel
from models.address_model import AddressModel
from models.img_model import ImgModel
from mappers.branch_mapper import BranchMapper
from mappers.address_mapper import AddressMapper
from mappers.img_mapper import ImgMapper
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
            model.img = ImgModel()
            model.img.id = model.id

        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()

        BranchMapper(model, view).model_mapping()
        AddressMapper(model.address, view.get('address', None)).model_mapping()
        ImgMapper(model.img, view.get('img', None)).model_mapping()
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
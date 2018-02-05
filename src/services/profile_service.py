from db import db
from utils.util import uid
from models.profile_model import ProfileModel
from models.branch_model import BranchModel
from models.address_model import AddressModel
from models.img_model import ImgModel

from mappers.profile_mapper import ProfileMapper
from mappers.img_mapper import ImgMapper
from mappers.branch_mapper import BranchMapper
from mappers.address_mapper import AddressMapper
import datetime

class ProfileService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if view.get('id', None) is not None:
            model = ProfileModel.query.filter_by(id=view.get('id')).first()
        if model is None:
            model = ProfileModel()
            model.id = uid()
            model.branch = BranchModel()
            model.branch.id = model.id
            model.img = ImgModel()
            model.img.id = model.id

        model.vid = self.session_info['vid']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()
        model.createdOn = datetime.datetime.now()

        ProfileMapper(model, view).model_mapping()
        BranchMapper(model.branch, view.get('branch', None)).model_mapping()
        ImgMapper(model.img, view.get('img', None)).model_mapping()
        return model

    def save(self, req_data):
        profile = self.mapping(None, req_data)
        db.session.add(profile)
        db.session.commit()
        return {'message': 'Saved Successfully', 'id': profile.id}


    def search(self):
        print("branch service")
        data_list = ProfileModel.query.all()
        print(data_list[0].__dict__)
        return data_list
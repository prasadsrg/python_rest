from db import db
from utils.util import uid
from models.profile_model import ProfileModel
from models.branch_model import BranchModel
from models.address_model import AddressModel
from models.img_model import ImgModel

from mappers.profile_mapper import ProfileMapper
from mappers.img_mapper import ImgMapper
from mappers.address_mapper import AddressMapper
import datetime

class ProfileService:

    session_info = None

    def mapping(self, model, view):
        print(self.session_info)
        if model.id is None:
            model = ProfileModel()
            model.id = uid()
            model.branchId = view['branch']['id']
            model.address = AddressModel()
            model.address.id = model.id
            model.address.vid = self.session_info['vid']
            model.img = ImgModel()
            model.img.id = model.id

        model.vid = self.session_info['vid']
        model.createdBy = self.session_info['id']
        model.updatedBy = self.session_info['id']
        model.updatedOn = datetime.datetime.now()
        model.createdOn = datetime.datetime.now()

        ProfileMapper(model, view).model_mapping()
        AddressMapper(model.address, view.get('address', None)).model_mapping()
        ImgMapper(model.img, view.get('img', None)).model_mapping()

    def isValidate(self, model):
        model.vid = self.session_info['vid']
        list = ProfileModel.query.filter(vid==model.vid, (mobile==model.mobile | email == model.email))
        if list:
            if model.id is None:
                return False;
            else:
                for item in list:
                    if item.id != model.id:
                        return False
        return True

    def save(self, req_data):
        profile = None
        _id = req_data('id', None);
        if _id is not None:
            profile = ProfileModel.query.filter_by(id=_id).first()
        if profile is None:
            profile = ProfileModel()
        if self.isValidate(profile):
            self.mapping(profile, req_data)
            db.session.add(profile)
            db.session.commit()
            return {'message': 'Saved Successfully', 'id': profile.id}
        else:
            raise Exception('Record already exists')

    def search(self):
        print("branch service")
        data_list = ProfileModel.query.all()
        return data_list

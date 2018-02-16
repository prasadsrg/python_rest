from db import session
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

    def isValidate(self, model, is_new):
        model.vid = self.session_info['vid']
        query = session.query(ProfileModel).filter(ProfileModel.vid==model.vid)\
            .filter((ProfileModel.mobile==model.mobile) | (ProfileModel.email == model.email))
        data_list = query.all()
        print(data_list)
        if data_list:
            if is_new:
                return False;
            else:
                for item in list:
                    if item.id != model.id:
                        return False
        return True

    def save(self, req_data):
        profile = None
        _id = req_data.get('id', None);
        is_new = True
        if _id is not None:
            profile = ProfileModel.query.filter_by(id=_id).first()
            is_new = False
        if profile is None:
            profile = ProfileModel()
            is_new = True
        self.mapping(profile, req_data)
        if self.isValidate(profile, is_new):
            session.add(profile)
            session.commit()
            return {'message': 'Saved Successfully', 'id': profile.id}
        else:
            raise Exception('Record already exists')

    def search(self):
        print("branch service")
        data_list = ProfileModel.query.all()
        return data_list

from db import db
import json
from models.branch_model import BranchModel
#from helpers.vendor_helper import VendorHelper


class BranchService:

    session_info = None

    # def save(self, req_data):
    #     vendor = None
    #     if req_data.get('id', None) is not None:
    #        vendor = VendorModel.query.filter_by(id=req_data.get('id')).first()
    #     if vendor is None:
    #         vendor = VendorModel()
    #
    #     VendorHelper(vendor, req_data).model_mapping()
    #     db.session.add(vendor)
    #     db.session.commit()
    #     return {'message': 'Saved Successfully'}


    def search(self):
        print("branch service")
        data_list = BranchModel.query.all()
        print(data_list[0].__dict__)
        return data_list
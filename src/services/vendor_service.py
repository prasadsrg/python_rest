from db import db
import json
from models.vendor_model import VendorModel
from helpers.vendor_helper import VendorHelper


class VendorService:

    session_info = None

    def save(self, req_data):
        vendor = None
        if req_data.get('id', None) is not None:
           vendor = VendorModel.query.filter_by(id=req_data.get('id')).first()
        if vendor is None:
            vendor = VendorModel()

        VendorHelper(vendor, req_data).model_mapping()
        db.session.add(vendor)
        db.session.commit()
        return {'message': 'Saved Successfully'}


    def search(self):
        data_list = VendorModel.query.all()
        print(data_list)
        return data_list
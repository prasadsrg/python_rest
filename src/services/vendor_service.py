from db import db
import json
from models.vendor_model import VendorModel
from helpers.vendor_helper import VendorHelper


class VendorService:

    session_info = None

    def save(self, req_data):
        try:
            vendor = None
            if req_data.get('id', None) is not None:
                vendor = VendorModel.query.filter_by(id=req_data.get('id')).first()
            print(vendor)
            if vendor is None:
                vendor = VendorModel()

            VendorHelper(vendor, req_data).model_mapping()
            db.session.add(vendor)
            db.session.commit()
            return {'message': 'Saved Successfully'}
        except Exception as e:
            print(e.args)
            return { 'message': e.args[0]}
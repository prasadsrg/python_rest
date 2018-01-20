from db import db
import json
from models.vendor_model import VendorModel
from helpers.vendor_helper import VendorHelper


class VendorService:

    session_info = None

    def save(self, req_data):
        try:
            vendor = VendorModel()
            VendorHelper.model_mapping(vendor, req_data)
            db.session.add(vendor)
            db.session.commit()
            return {'message': 'Saved Successfully'}
        except Exception as e:
            print(e.args)
            return { 'message': e.args[0]}
from db import db

class ConsumerModel(db.Model):
    __tablename__ = 'consumer'

    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String)
    mobile = db.Column('mobile', db.String)
    email = db.Column('email', db.String)
    aadhar = db.Column('aadhar', db.String)
    imgId = db.Column('img_id', db.String)
    addressId = db.Column('address_id', db.String)
    active = db.Column('active', db.Boolean)
    vid = db.Column('vid', db.String)
    createdOn = db.Column('created_on', db.DateTime)
    updatedBy = db.Column('updated_by', db.String)
    updatedOn = db.Column('updated_on', db.DateTime)
from db import db

class ApexDataModel(db.Model):
    __tablename__ = 'apex_data'

    name = db.Column('name', db.String)
    code = db.Column('code', db.String)
    status = db.Column('status', db.Boolean)
from db import db
from models.apex_report_model import ApexReportModel

class ApexReportDataModel(db.Model):
    __tablename__ = 'apex_report_data'

    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String)
    status = db.Column('status', db.Boolean)
    apexReportId = db.Column('apex_report_id', db.String, db.ForeignKey('apex_report_id.id'))
    apexReport = db.relationship(ApexReportModel)
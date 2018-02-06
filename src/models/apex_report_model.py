from db import db

class ApexReportModel(db.Model):
    __tablename__ = 'apex_report'

    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String)
    reportUrl = db.Column('report_url', db.String)
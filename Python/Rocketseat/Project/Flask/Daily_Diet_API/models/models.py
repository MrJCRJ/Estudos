from main import db
from datetime import datetime

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_within_diet = db.Column(db.Boolean, default=True)

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    send_time = db.Column(db.DateTime, nullable=False)
    method = db.Column(db.String(10), nullable=False)
    sent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Reminder {self.id} to {self.recipient} at {self.send_time}>"
    
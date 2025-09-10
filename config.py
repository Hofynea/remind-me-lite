import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reminders.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
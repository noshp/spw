import os

DEBUG = bool(os.environ.get('DEBUG'))
SQLALCHEMY_DATABASE_URI = str(os.environ.get('SQLALCHEMY_DATABASE_URI'))
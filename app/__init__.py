from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

#Initialize the app
app = Flask(__name__, instance_relative_config=True)

#Load the views
from app import views

#load the config file
app.config.from_object('config')
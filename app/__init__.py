from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

#Initialize the app
app = Flask(__name__, instance_relative_config=True)

#Load the views
from app import views

#load the config file
app.config.from_object('config')
from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

#Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'ADD_THE_AWS_PG_CONNECTION_STRING_HERE'
db = SQLAlchemy(app)
#load the config file
#app.config.from_object('config')

#Load the views
from app import views
from app.models import *

#Create the Flask-Restless API Manager
manager = APIManager(app, flask_sqlalchemy_db=db)

#All the endpoints can be accessed under /api/[tablename]
manager.create_api(UniversityEmploymentRates, methods=['GET'])
manager.create_api(UniversityProgramList, methods=['GET'])
manager.create_api(NOCSynonymList, methods=['GET'])
manager.create_api(NOCList, methods=['GET'])
manager.create_api(SkillLevelList, methods=['GET'])
manager.create_api(TaskList, methods=['GET'])
manager.create_api(EssentialSkills, methods=['GET'])
manager.create_api(TotalJobOpenings, methods=['GET'])
manager.create_api(NOCLocationList, methods=['GET'])
manager.create_api(NOCSalaryList, methods=['GET'])
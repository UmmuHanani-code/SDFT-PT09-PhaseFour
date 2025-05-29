from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from server.views.employee_view import EmployeeResourceView, FetchAllEmployeeResourceView
import os

employee_api = Flask(__name__)
api = Api(employee_api)

basedir = os.path.abspath(os.path.dirname(__file__))
employee_api.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "employee_api.db")}'
employee_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
employee_api.config['SECRET_KEY'] = 'zeraki-forces-secret'
employee_api.json.compact = False

db.init_app(employee_api)
migrate = Migrate(employee_api, db)

api.add_resource(FetchAllEmployeeResourceView, "/api/employee")
api.add_resource(EmployeeResourceView, "/api/employee/<int:employee_id>")

if __name__ == "__main__":
    employee_api.run()

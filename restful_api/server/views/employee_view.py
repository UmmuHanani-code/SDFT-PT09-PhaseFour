from flask_restful import Resource, request
from controllers.employee_services import EmployeeController, HomeController



class HomeView(Resource):
    def get(self):
        return HomeController.homepage()

class EmployeeResourceView(Resource):
    def get (self, employee_id):

        return EmployeeController.get_employee(employee_id), 200

    def put(self, employee_id):
        data = request.get_json()
        return EmployeeController.update_employee(employee_id, data), 200

    def delete(self, employee_id):
        return EmployeeController.delete_employee(employee_id), 200


class FetchAllEmployeeResourceView(Resource):
    def get(self):
        return EmployeeController.get_all_employees(), 200

    def post(self):
        data = request.get_json()
        return EmployeeController.create_employee(data), 201


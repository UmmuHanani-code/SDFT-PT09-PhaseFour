from flask_restful import Resource, reqparse
from server.controllers.employee_services import EmployeeController


class EmployeeResourceView(Resource):
    
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

class FetchAllEmployeeResourceView(Resource):
    
    def get(self):
        return EmployeeController.get_all_employees()


    def post(self):
        pass

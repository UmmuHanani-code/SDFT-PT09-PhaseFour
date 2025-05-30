# SOLID Principles

from models import db, Employee
from flask import abort

class HomeController:
    @staticmethod
    def homepage():
        return {"message": "Welcome to the Employee API!"}, 200

class EmployeeController:
    @staticmethod
    def homepage():
        return {"message": "Welcome to the Employee API!"}, 200
    @staticmethod
    def get_all_employees():
        employees = Employee.query.all()
        return [employee.to_dict() for employee in employees]

    @staticmethod
    def get_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            abort(404, description="Employee not found")
        return employee.to_dict()

    @staticmethod
    def create_employee(data):
        if Employee.query.filter_by(email=data['email']).first():
            abort(400, description="Email already exists")

        employee = Employee(
            name=data['name'],
            email=data['email'],
            department=data['department'],
            salary=data['salary']
        )
        db.session.add(employee)
        db.session.commit()
        return employee.to_dict()

    @staticmethod
    def update_employee(employee_id, data):
        employee = Employee.query.get(employee_id)
        if not employee:
            abort(404, description="Employee not found")

        if 'email' in data and data['email'] != employee.email and Employee.query.filter_by(email=data['email']).first():
            abort(400, description="Email already exists")

        employee.name = data.get('name', employee.name)
        employee.email = data.get('email', employee.email)
        employee.department = data.get('department', employee.department)
        employee.salary = data.get('salary', employee.salary)
        db.session.commit()
        return employee.to_dict()

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            abort(404, description="Employee not found")
        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted successfully"}

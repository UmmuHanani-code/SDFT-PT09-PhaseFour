from sqlalchemy_serializer import SerializerMixin
from models.db import db

class Employee(db.Model, SerializerMixin):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    department =db.Column(db.String)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.email}, {self.department}, {self.salary} >"

from sqlalchemy_serializer import SerializerMixin
from .db import db

class Employee(db.Model, SerializerMixin):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Employee {self.id} {self.name}>"

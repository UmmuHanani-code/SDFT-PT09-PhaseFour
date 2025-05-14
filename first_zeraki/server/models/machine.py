from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone
from .db import db

class Machine(db.Model, SerializerMixin):
    __tablename__ = "machines"
    serialize_only = ("id", "type", "serial_number", "status", "soldier.name")

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    serial_number = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, default='Operational')
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # foreign key tha points to the one side
    soldier_id = db.Column(db.Integer, db.ForeignKey('soldiers.id'), nullable=False)

    # Realtionship
    soldier = db.relationship("Soldier", back_populates="machines")


    def __repr__(self):
        return f'<Machine {self.id}, {self.type}, {self.status}>'
    
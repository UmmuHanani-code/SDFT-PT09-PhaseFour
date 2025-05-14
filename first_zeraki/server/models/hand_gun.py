from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone
from .db import db

class HandGun(db.Model, SerializerMixin):
    __tablename__ = "handguns"
    serialize_only = ("id", "serial_number", "soldier.name")

    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))    
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # foreign key to belongs to realtionship
    solidier_id = db.Column(db.Integer, db.ForeignKey("soldiers.id"), nullable=False)

    # belong to relationship
    soldier = db.relationship('Soldier', back_populates="handgun")

    def __repr__(self):
        return f"<HandGun {self.id}, {self.serial_number}>"
    

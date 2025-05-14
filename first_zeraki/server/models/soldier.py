from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone
from .db import db


class Soldier(db.Model, SerializerMixin):
    __tablename__ = "soldiers"
    serialize_only = ('id', 'name', 'rank', 'handgun.serial_number', 'machines.type')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))    
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # has one relationship
    handgun = db.relationship("HandGun", back_populates="soldier", uselist=False, cascade="all, delete-orphan")

    # has many relationship
    machines = db.relationship("Machine", back_populates="soldier", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Soldier {self.id}, {self.name}, {self.rank}>"
    
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone
from .db import db
from .join_table import soldier_team


class Soldier(db.Model, SerializerMixin):
    __tablename__ = "soldiers"
    serialize_only = ('id', 'name', 'rank', 'handgun.serial_number', 'machines.type', "teams.name")
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))    
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # has one relationship
    handgun = db.relationship("HandGun", back_populates="soldier", uselist=False, cascade="all, delete-orphan")

    # has many relationship
    machines = db.relationship("Machine", back_populates="soldier", cascade="all, delete-orphan")

    # connection to the team through the join table
    teams = db.relationship(
        "Team",
        secondary=soldier_team,
        back_populates="soldiers"
    )

    # connection to the mission through the Association object
    mission_associations = db.relationship(
        'SoldierMission',
        back_populates='soldier',
        cascade='all, delete-orphan',
        lazy='select'
    )

    def __repr__(self):
        return f"<Soldier {self.id}, {self.name}, {self.rank}>"
    
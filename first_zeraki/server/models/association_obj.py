from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class SoldierMission(db.Model, SerializerMixin):
    __tablename__ = "soldier_mission"
    serialize_only = ('soldier_id', 'mission_id', 'role', 'assigned_date', 'status', 'soldier.name', 'mission.name')

    # Foreign keys as primary keys for uniqueness
    soldier_id = db.Column(db.Integer, db.ForeignKey('soldiers.id'), primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey('missions.id'), primary_key=True)
    # Extra details
    role = db.Column(db.String(50), nullable=False, default='Operative')
    assigned_date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(50), nullable=False, default='Active')  # e.g., Active, Completed

    # Relationships
    soldier = db.relationship('Soldier', back_populates='mission_associations', lazy='select')
    mission = db.relationship('Mission', back_populates='soldier_associations', lazy='select')

    def __repr__(self):
        return f"<SoldierMission soldier={self.soldier_id}, mission={self.mission_id}, role={self.role}, status={self.status}>"
    
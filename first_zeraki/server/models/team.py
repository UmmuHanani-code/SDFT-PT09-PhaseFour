from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone
from .db import db
from .join_table import soldier_team


class Team(db.Model, SerializerMixin):
    __tablename__ = "teams"
    serialize_only = ("id", "name", "soldiers.name")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # connect to the soldier through the join table
    soldiers = db.relationship(
        "Soldier",
        secondary=soldier_team,
        back_populates="teams"
    )

    def __repr__(self):
        return f'<Team {self.id}, {self.name}>'

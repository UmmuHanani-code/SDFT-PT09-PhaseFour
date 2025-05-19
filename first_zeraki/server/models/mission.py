from models.db import db
from sqlalchemy_serializer import SerializerMixin

class Mission(db.Model, SerializerMixin):
    __tablename__ = "missions"
    serialize_only = ('id', 'name', 'description', 'soldier_associations.soldier.name')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # e.g., Operation Night Hawk
    description = db.Column(db.Text, nullable=True)  # Mission details

    # One-to-many with SoldierMission
    soldier_associations = db.relationship(
        'SoldierMission',
        back_populates='mission',
        cascade='all, delete-orphan',
        lazy='select'
    )

    def __repr__(self):
        return f"<Mission {self.id}, {self.name}>"
    
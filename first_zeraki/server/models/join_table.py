from .db import db

# The join/association table
soldier_team = db.Table(
    "soldier_team",
    db.Column("soldier_id", db.Integer, db.ForeignKey('soldiers.id'), primary_key=True),
    db.Column("team_id", db.Integer, db.ForeignKey('teams.id'), primary_key=True)
)

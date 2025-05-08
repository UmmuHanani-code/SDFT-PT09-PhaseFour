# server/seed.py
from random import choice
from faker import Faker
from app import zeraki, db
from models.soldier import Soldier

# Setup logging

fake = Faker()
ranks = ['Sergeant', 'Staff Sergeant', 'Lieutenant', 'Captain']

with zeraki.app_context():
    try:

        Soldier.query.delete()
        db.session.commit()

        soldiers = [Soldier(name=fake.name(), rank=choice(ranks)) for _ in range(100)]
        db.session.add_all(soldiers)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        raise
#!/usr/bin/env python3
import logging
from random import choice, sample
from faker import Faker
from app import zeraki, db
from models.soldier import Soldier
from models.machine import Machine
from models.hand_gun import HandGun
from models.team import Team, soldier_team


# Initialize Faker
fake = Faker()

# Predefined ranks for soldiers
ranks = ['Sergeant', 'Staff Sergeant', 'Lieutenant', 'Captain']

# Predefined machine types and statuses
machine_types = ['Drone', 'Tank', 'Jeep', 'Robot', 'APC']
machine_statuses = ['Operational', 'Maintenance', 'Decommissioned']
team_names = ['Alpha Squad', 'Bravo Team', 'Charlie Unit']

with zeraki.app_context():
    try:
        db.session.execute(soldier_team.delete())
        Machine.query.delete()
        HandGun.query.delete()
        Soldier.query.delete()
        Team.query.delete()
        db.session.commit()

        # Create teams
        teams = [Team(name=name) for name in team_names]
        db.session.add_all(teams)
        db.session.commit()

        # Create soldiers
        soldiers = [
            Soldier(
                name=fake.name(),
                rank=choice(ranks)
            ) for _ in range(100)
        ]
        db.session.add_all(soldiers)
        db.session.commit()

        # Create handguns (one-to-one with Soldier)
        handguns = []
        for i, soldier in enumerate(soldiers[:80]):  # Assign handguns to 80% of soldiers
            handguns.append(
                HandGun(
                    serial_number=f"HG{fake.unique.random_int(min=1000, max=9999)}",
                    soldier=soldier
                )
            )
        db.session.add_all(handguns)
        db.session.commit()

        # Create machines (one-to-many with Soldier)
        machines = []
        for soldier in soldiers[:90]:  # Assign machines to 90% of soldiers
            num_machines = choice([1, 2, 3])  # Randomly assign 1-3 machines
            for _ in range(num_machines):
                machines.append(
                    Machine(
                        type=choice(machine_types),
                        serial_number=f"{choice(machine_types[:3]).upper()}{fake.unique.random_int(min=100, max=999)}",
                        status=choice(machine_statuses),
                        soldier=soldier
                    )
                )
        db.session.add_all(machines)
        db.session.commit()

        # connect soldier to teams
        for soldier in soldiers:
            assigned_teams = sample(teams, k=choice([1, 2]))
            soldier.teams.extend(assigned_teams)  # Adds rows to soldier_team
        db.session.commit()

  
    except Exception as e:
        db.session.rollback()
        raise

from model import SkillList, PublicTeam, MentorList
from settings import DB_NAME

import requests

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()


def add_skills():
    req = requests.get('https://hackbulgaria.com/hackfmi/api/skills/')

    for row in req.json():
        s = SkillList(name=row['name'])
        session.add(s)
        session.commit()


def add_public_team():
    req = requests.get('https://hackbulgaria.com/hackfmi/api/public-teams/')

    for row in req.json():
        p = PublicTeam(name=row['name'],
                       idea_description=row['idea_description'],
                       repository=row['repository'],
                       need_more_members=row['need_more_members'],
                       members_needed_desc=row['members_needed_desc'],
                       room=row['room'],
                       place=row['place'])
        if row['technologies_full']:
            for el in row['technologies_full']:
                s = session.query(SkillList)\
                           .filter(SkillList.name == el['name']).one()
                p.technologies_full.append(s)
        session.add(p)
        session.commit()


def add_mentor_list():
    req = requests.get('https://hackbulgaria.com/hackfmi/api/mentors/')

    for row in req.json():
        m = MentorList(name=row['name'],
                       description=row['description'],
                       picture=row['picture'])
        if row['teams']:
            for el in row['teams']:
                p = session.query(PublicTeam)\
                           .filter(PublicTeam.name == el['name']).one()
                m.teams.append(p)
        session.add(m)
        session.commit()


def main():
    add_skills()
    add_public_team()
    add_mentor_list()
    pass


if __name__ == '__main__':
    main()

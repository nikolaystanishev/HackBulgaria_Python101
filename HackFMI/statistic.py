from model import SkillList, PublicTeam, MentorList, team_skills_table,\
    Member, mentor_teams_table
from settings import DB_NAME

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()


def get_teams_in_room(room):
    s = session.query(PublicTeam).filter(PublicTeam.room == room).count()
    return s


def get_team_with_skill(skill):
    s = session.query(team_skills_table).join(SkillList)\
               .filter(SkillList.name == skill).count()
    return s


def team_member_to_team(team, member):
    s = Member(name=member, team=team)
    session.add(s)
    session.commit()


def add_skill_to_team(team, skill):
    s = session.query(PublicTeam).filter(PublicTeam.id == team).one()
    s.technologies_full.append(session.query(SkillList)
                                      .filter(SkillList.name == skill).one())
    session.commit()


def get_info_for_mentor_teams(mentor):
    s = session.query(mentor_teams_table).join(MentorList)\
               .filter(MentorList.name == mentor)
    result = []
    for team in s:
        result.append(session.query(PublicTeam)
                             .filter(PublicTeam.id == team.PublicTeam_id)
                             .one().name)
    return result


def get_info_for_mentor_rooms(mentor):
    s = session.query(mentor_teams_table).join(MentorList)\
               .filter(MentorList.name == mentor)
    result = []
    for team in s:
        result.append(session.query(PublicTeam)
                             .filter(PublicTeam.id == team.PublicTeam_id)
                             .one().room)
    return sorted(result)


def add_mentor(*args, **kwargs):
    m = MentorList()
    if 'name' in kwargs:
        m.name = kwargs['name']
    if 'description' in kwargs:
        m.description = kwargs['description']
    if 'picture' in kwargs:
        m.picture = kwargs['picture']
    if 'teams' in kwargs:
        for el in kwargs['teams']:
            p = session.query(PublicTeam)\
                       .filter(PublicTeam.name == el['name']).one()
            m.teams.append(p)
    session.add(m)
    session.commit()


def add_team(*args, **kwargs):
    p = PublicTeam()
    if 'name' in kwargs:
        p.name = kwargs['name']
    if 'idea_description' in kwargs:
        p.idea_description = kwargs['idea_description']
    if 'repository' in kwargs:
        p.repository = kwargs['repository']
    if 'need_more_members' in kwargs:
        p.need_more_members = kwargs['need_more_members']
    if 'members_needed_desc' in kwargs:
        p.members_needed_desc = kwargs['members_needed_desc']
    if 'room' in kwargs:
        p.room = kwargs['room']
    if 'place' in kwargs:
        p.place = kwargs['place']
    if 'technologies_full' in kwargs:
        for el in kwargs['technologies_full']:
            s = session.query(SkillList)\
                       .filter(SkillList.name == el['name']).one()
            p.technologies_full.append(s)
    session.add(p)
    session.commit()


def add_skill(*args, **kwargs):
    if 'name' in kwargs:
        s = SkillList(name=kwargs['name'])
        session.add(s)
        session.commit()


def main():
    print(get_teams_in_room('2'))
    add_skill_to_team(1, 'C/C++')
    print(get_team_with_skill('C/C++'))
    team_member_to_team(1, 'Panda')
    s = get_info_for_mentor_teams('Анна-Мария Ангелова')
    for team in s:
        print(team)
    r = get_info_for_mentor_rooms('Анна-Мария Ангелова')
    for room in r:
        print(room)
    add_mentor(name='Panda')
    add_team(name='Panda')
    add_skill(name='Panda')


if __name__ == '__main__':
    main()

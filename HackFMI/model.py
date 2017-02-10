from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base


mentor_teams_table = Table('mentor_teams', Base.metadata,
                           Column('MentorList_id', Integer,
                                  ForeignKey('MentorList.id')),
                           Column('PublicTeam_id', Integer,
                                  ForeignKey('PublicTeam.id')))


class MentorList(Base):
    __tablename__ = 'MentorList'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    picture = Column(String)
    teams = relationship('PublicTeam', secondary=mentor_teams_table,
                         back_populates='mentor')


team_skills_table = Table('team_skills', Base.metadata,
                          Column('PublicTeam_id', Integer,
                                 ForeignKey('PublicTeam.id')),
                          Column('SkillList_id', Integer,
                                 ForeignKey('SkillList.id')))


class PublicTeam(Base):
    __tablename__ = 'PublicTeam'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    idea_description = Column(String)
    repository = Column(String)
    technologies_full = relationship('SkillList', secondary=team_skills_table,
                                     back_populates='publicteam')
    need_more_members = Column(Boolean)
    members_needed_desc = Column(String)
    room = Column(String)
    place = Column(String)
    mentor = relationship('MentorList', secondary=mentor_teams_table,
                          back_populates='teams')


class SkillList(Base):
    __tablename__ = 'SkillList'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    publicteam = relationship('PublicTeam', secondary=team_skills_table,
                              back_populates='technologies_full')


class Member(Base):
    __tablename__ = 'Member'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    team = Column(Integer, ForeignKey('PublicTeam.id'))

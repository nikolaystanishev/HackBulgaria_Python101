from sqlalchemy import Column, Integer, String, REAL

from base import Base


class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    email = Column(String, nullable=True)
    balance = Column(REAL, default=0)
    message = Column(String)
    reset_code = Column(String)
    tan_code = Column(String, default=None)

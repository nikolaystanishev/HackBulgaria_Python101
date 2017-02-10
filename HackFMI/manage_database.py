from sqlalchemy import create_engine

from base import Base

import model
from settings import DB_NAME

engine = create_engine(DB_NAME)

Base.metadata.create_all(engine)

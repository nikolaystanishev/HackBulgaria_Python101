import sqlite3
from settings.sql_creation_settings import DB_NAME
import queries.manage_db_queries as queries


class Projections:
    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def show_projections(self, movie_id, projection_date='%-%'):
        projections = queries.SELECT_PROJECTIONS_ORDERED_BY_DATE
        result = self.c.execute(projections, (movie_id, projection_date))
        return result

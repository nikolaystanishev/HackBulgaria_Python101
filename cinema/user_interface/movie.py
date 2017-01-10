import sqlite3
from settings.sql_creation_settings import DB_NAME
import queries.manage_db_queries as queries


class Movie:
    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def show_movies(self):
        movies = queries.SELECT_MOVIES_ORDERED_BY_RATING
        result = self.c.execute(movies)
        return result

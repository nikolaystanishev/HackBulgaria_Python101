import sqlite3
from settings.sql_creation_settings import DB_NAME
import queries.manage_db_queries as queries


class Reservations:
    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def get_taken_seats(self, projection):
        available_seats = queries.SELECT_AVAILABLE_SEATS
        result = self.c.execute(available_seats, (projection,))
        return result

    def reservation(self, reservation_data):
        insert_resevations = queries.INSERT_INTO_RESERVATIONS_TABLE
        self.c.executemany(insert_resevations, reservation_data)
        self.db.commit()

import sqlite3
import queries.create_db_queries as queries
import queries.manage_db_queries as insert_queries
import settings.insert_values as insert_values
from settings.sql_creation_settings import DB_NAME

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def create_tables(drop_query, create_query):
    c.execute(drop_query)
    c.execute(create_query)
    db.commit()


def create_database():
    create_tables(queries.DROP_MOVIES_TABLE,
                  queries.CREATE_MOVIES_TABLE)
    create_tables(queries.DROP_PROJECTIONS_TABLE,
                  queries.CREATE_PROJECTIONS_TABLE)
    create_tables(queries.DROP_USERS_TABLE,
                  queries.CREATE_USERS_TABLE)
    create_tables(queries.DROP_RESERVATIONS_TABLE,
                  queries.CREATE_RESERVATIONS_TABLE)


def insert_in_table(query, insert_values):
    c.executemany(query, insert_values)
    db.commit()


def insert_in_database():
    insert_in_table(insert_queries.INSERT_INTO_MOVIES_TABLE,
                    insert_values.movies)
    insert_in_table(insert_queries.INSERT_INTO_PROJECTIONS_TABLE,
                    insert_values.projections)
    insert_in_table(insert_queries.INSERT_INTO_USERS_TABLE,
                    insert_values.users)
    insert_in_table(insert_queries.INSERT_INTO_RESERVATIONS_TABLE,
                    insert_values.reservations)


def main():
    create_database()
    insert_in_database()
    db.close()

if __name__ == '__main__':
    main()

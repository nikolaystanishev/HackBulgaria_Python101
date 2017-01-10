movie_col = ['Id', 'Name', 'Rating']
projection_col = ['Id', 'Movie_ID', 'Type', 'Projections Date',
                  'Projections Time', 'Available Spots']

options = ['show movies', 'show movie projection <movieid> '
           '[<projection date>]', 'make reservation', 'help', 'exit']

available_seat = '.'
taken_seat = 'x'

number_of_rows = 10
number_of_cols = 10


def get_seats():
    seats = []
    for i in range(number_of_rows):
        seats.append(list(number_of_cols*available_seat))
    return seats

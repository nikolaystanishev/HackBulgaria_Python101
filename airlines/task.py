class Flight:

    def __init__(self, start_time, end_time, passengers, max_passengers,
                 from_dest, to_dest, terminal, declined):
        self.start_time = start_time
        self.end_time = end_time
        self.num_of_passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.passengers = []

    def set_passengers(self, passenger):
        self.passengers.append(passenger)

    def flight_duration(self):
        hours = int(self.end_time.hour.split(':')[0]) -\
                int(self.start_time.hour.split(':')[0])
        minutes = int(self.end_time.hour.split(':')[1]) -\
            int(self.start_time.hour.split(':')[1])
        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            hours += 24
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        return "{}:{}".format(hours, minutes)


class Date:

    def __init__(self, day, month, year, hour):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour


class Terminal:

    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights


class Passenger:

    def __init__(self, first_name, last_name, flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age


class Reservation:

    def __init__(self, flight, passenger, accepted):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted


class All_Flights:

    def __init__(self):
        self.flights = []

    def set_flight(self, flight):
        self.flights.append(flight)

    def get_flights_for(self, date):
        result = []
        for flight in self.flights:
            if flight.start_time.day == date.day and\
               flight.start_time.month == date.month and\
               flight.start_time.year == date.year:
                result.append(flight)
        return result

    def get_flight_before(self, date, hour):
        result = []
        for flight in self.flights:
            if flight.start_time.day == date.day and\
               flight.start_time.month == date.month and\
               flight.start_time.year == date.year and\
               flight.start_time.hour < hour:
                result.append(flight)
        return result

    def get_flight_from_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.from_dest == destination:
                result.append(flight)
        return result

    def get_flight_to_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination:
                result.append(flight)
        return result

    def get_flight_to(self, destination, date):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination and\
               flight.end_time.day == date.day and\
               flight.end_time.month == date.month and\
               flight.end_time.year == date.year and\
               flight.end_time.hour == date.hour:
                result.append(flight)
        return result

    def get_flight_from(self, destination, date):
        result = []
        for flight in self.flights:
            if flight.from_dest == destination and\
               flight.start_time.day == date.day and\
               flight.start_time.month == date.month and\
               flight.start_time.year == date.year and\
               flight.start_time.hour == date.hour:
                result.append(flight)
        return result

    def get_terminal_flights(self, terminal_number):
        result = []
        for flight in self.flights:
            if flight.terminal.number == terminal_number:
                result.append(flight)
        return result

    def get_terminal_flights_on(self, terminal_number, date):
        result = []
        for flight in self.flights:
            if flight.start_time.day == date.day and\
               flight.start_time.month == date.month and\
               flight.start_time.year == date.year and\
               flight.terminal.number == terminal_number:
                result.append(flight)
        return result

    def terminal_flights_to_dest(self, terminal_number, destination):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination and\
               flight.terminal.number == terminal_number:
                result.append(flight)
        return result

    def flights_within_duration(self, start_time, end_time):
        result = []
        for flight in self.flights:
            if flight.start_time.year >= start_time.year and\
               flight.end_time.year <= end_time.year:
                if flight.start_time.month >= start_time.month and\
                   flight.end_time.month <= end_time.month:
                    if flight.start_time.day >= start_time.day and\
                       flight.end_time.day <= end_time.day:
                        if flight.start_time.hour >= start_time.hour and\
                           flight.end_time.hour <= end_time.hour:
                            result.append(flight)
        return result

    def passengers_under_18(self, flight):
        result = 0
        for passenger in flight.passengers:
            if passenger.age <= 18:
                result += 1
        return result

    def passengers_to_dest(self, destination):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination:
                for passenger in flight.passengers:
                    result.append(passenger)
        return result

    def passengers_from_terminal(self, terminal_number):
        result = []
        for flight in self.flights:
            if flight.terminal.number == terminal_number:
                for passenger in flight.passengers:
                    result.append(passenger)
        return result

    def flights_with_passengers(self, size):
        result = []
        for flight in self.flights:
            if flight.num_of_passengers < size:
                for passenger in flight.passengers:
                    result.append(passenger)
        return result

    def passengers_reservations(self, flight):
        result = []
        for passenger in flight.passengers:
            result.append(passenger)
        return result

    def reservations_to_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination:
                for passenger in flight.passengers:
                    result.append(passenger)
        return result

    def flight_empty_seats(self, flight):
        if flight.num_of_passengers < flight.max_passengers:
            return True
        return False

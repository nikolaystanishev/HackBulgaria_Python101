import unittest
from task import *


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.start_time = Date(29, 11, 2016, hour='12:20')
        self.end_time = Date(29, 11, 2016, hour='15:30')
        self.terminal = Terminal(2, 30)
        self.flight = Flight(start_time=self.start_time,
                             end_time=self.end_time,
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=self.terminal, declined=False)
        self.passenger = Passenger(first_name="Rositsa", last_name="Zlateva",
                                   flight=self.flight, age=22)
        self.flight.set_passengers(self.passenger)

    def test_flight_init(self):
        self.assertEqual(self.flight.num_of_passengers, 100)
        self.assertEqual(self.flight.start_time, self.start_time)
        self.assertEqual(self.flight.end_time, self.end_time)
        self.assertEqual(self.flight.max_passengers, 120)
        self.assertEqual(self.flight.from_dest, "Sofia")
        self.assertEqual(self.flight.to_dest, "London")
        self.assertEqual(self.flight.terminal, self.terminal)
        self.assertEqual(self.flight.declined, False)

    def test_all_flights_set_passengers(self):
        self.assertEqual(self.flight.passengers[-1], self.passenger)

    def test_flight_flight_duration(self):
        self.assertEqual(self.flight.flight_duration(), "03:10")


class TestDate(unittest.TestCase):

    def setUp(self):
        self.start_time = Date(29, 11, 2016, hour='12:20')
        self.end_time = Date(29, 11, 2016, hour='15:30')

    def test_date_init(self):
        self.assertEqual(self.start_time.day, 29)
        self.assertEqual(self.start_time.month, 11)
        self.assertEqual(self.start_time.year, 2016)
        self.assertEqual(self.start_time.hour, '12:20')


class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.terminal = Terminal(2, 30)

    def test_terminal_init(self):
        self.assertEqual(self.terminal.number, 2)
        self.assertEqual(self.terminal.max_flights, 30)


class TestPassenger(unittest.TestCase):

    def setUp(self):
        self.start_time = Date(29, 11, 2016, hour='12:20')
        self.end_time = Date(29, 11, 2016, hour='15:30')
        self.terminal = Terminal(2, 30)
        self.flight = Flight(start_time=self.start_time,
                             end_time=self.end_time,
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=self.terminal, declined=False)
        self.passenger = Passenger(first_name="Rositsa", last_name="Zlateva",
                                   flight=self.flight, age=22)

    def test_passenger_init(self):
        self.assertEqual(self.passenger.first_name, "Rositsa")
        self.assertEqual(self.passenger.last_name, "Zlateva")
        self.assertEqual(self.passenger.flight, self.flight)
        self.assertEqual(self.passenger.age, 22)


class TestReservation(unittest.TestCase):

    def setUp(self):
        self.start_time = Date(29, 11, 2016, hour='12:20')
        self.end_time = Date(29, 11, 2016, hour='15:30')
        self.terminal = Terminal(2, 30)
        self.flight = Flight(start_time=self.start_time,
                             end_time=self.end_time,
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=self.terminal, declined=False)
        self.passenger = Passenger(first_name="Rositsa", last_name="Zlateva",
                                   flight=self.flight, age=22)
        self.reservation = Reservation(flight=self.flight,
                                       passenger=self.passenger,
                                       accepted=True)

    def test_reservation_init(self):
        self.assertEqual(self.reservation.flight, self.flight)
        self.assertEqual(self.reservation.passenger, self.passenger)
        self.assertEqual(self.reservation.accepted, True)


class TestAll_Flights(unittest.TestCase):

    def setUp(self):
        self.start_time = Date(29, 11, 2016, hour='12:20')
        self.end_time = Date(29, 11, 2016, hour='15:30')
        self.terminal = Terminal(2, 30)
        self.flight = Flight(start_time=self.start_time,
                             end_time=self.end_time,
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=self.terminal, declined=False)
        self.all_flights = All_Flights()
        self.all_flights.set_flight(self.flight)
        self.passenger = Passenger(first_name="Rositsa", last_name="Zlateva",
                                   flight=self.flight, age=22)
        self.flight.set_passengers(self.passenger)

    def test_all_flights_set_flight(self):
        self.assertEqual(self.all_flights.flights[-1], self.flight)

    def test_all_flights_get_flights_for(self):
        self.assertEqual(self.all_flights.get_flights_for(Date(29, 11, 2016,
                         hour='12:20')), [self.flight])

    def test_all_flights_get_flight_before(self):
        self.assertEqual(self.all_flights.get_flight_before(Date(29, 11, 2016,
                         hour='12:20'), '16:30'), [self.flight])

    def test_all_flights_get_flight_from_destination(self):
        self.assertEqual(self.all_flights.get_flight_from_destination("Sofia"),
                         [self.flight])

    def test_all_flights_get_flight_to_destination(self):
        self.assertEqual(self.all_flights.get_flight_to_destination("London"),
                         [self.flight])

    def test_all_flights_get_flight_to(self):
        self.assertEqual(self.all_flights.get_flight_to("London",
                         Date(29, 11, 2016, hour='15:30')), [self.flight])

    def test_all_flights_get_flight_from(self):
        self.assertEqual(self.all_flights.get_flight_from("Sofia",
                         Date(29, 11, 2016, hour='12:20')), [self.flight])

    def test_all_flights_get_terminal_flights(self):
        self.assertEqual(self.all_flights.get_terminal_flights(2),
                         [self.flight])

    def test_all_flights_get_terminal_flights_on(self):
        self.assertEqual(self.all_flights.get_terminal_flights_on(2,
                         Date(29, 11, 2016, hour='12:20')), [self.flight])

    def test_flight_terminal_flights_to_dest(self):
        self.assertEqual(self.all_flights.terminal_flights_to_dest(2,
                         "London"), [self.flight])

    def test_flight_flights_within_duration(self):
        self.assertEqual(self.all_flights.flights_within_duration(
                         Date(29, 11, 2016, hour='12:20'),
                         Date(29, 11, 2016, hour='15:30')), [self.flight])

    def test_flight_passengers_under_18(self):
        self.assertEqual(self.all_flights.passengers_under_18(self.flight), 0)

    def test_flight_passengers_to_dest(self):
        self.assertEqual(self.all_flights.passengers_to_dest("London"),
                         [self.passenger])

    def test_flight_passengers_from_terminal(self):
        self.assertEqual(self.all_flights.passengers_from_terminal(2),
                         [self.passenger])

    def test_flight_flights_with_passengers(self):
        self.assertEqual(self.all_flights.flights_with_passengers(200),
                         [self.passenger])

    def test_flight_passengers_reservations(self):
        self.assertEqual(self.all_flights.passengers_reservations(self.flight),
                         [self.passenger])

    def test_flight_reservations_to_destination(self):
        self.assertEqual(self.all_flights.reservations_to_destination
                         ("London"), [self.passenger])

    def test_flight_flight_empty_seats(self):
        self.assertEqual(self.all_flights.flight_empty_seats(self.flight),
                         True)


if __name__ == "__main__":
    unittest.main()

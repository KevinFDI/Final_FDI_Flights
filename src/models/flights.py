class Flights:

    def __init__(self, aircraft, arrival_code, date_created, departs_code, flight_id) -> None:
        self.aircraft = aircraft
        self.arrival_code = arrival_code
        self.date_created = date_created
        self.departs_code = departs_code
        self.flight_id = flight_id


    def serialize(self):
        return {
            'aircraft': self.aircraft,
            'arrival_code': self.arrival_code,
            'date_created': self.date_created,
            'departs_code': self.departs_code,
            'flight_id': self.flight_id
        }
class Flight:
    def __init__(self, db):
        self.db = db

    def add(self, num, origin, dest, dep_time, arr_time):
        self.db.execute_query('''INSERT INTO Flights (flight_number, origin, destination, departure_time, arrival_time)
                                 VALUES (?, ?, ?, ?, ?)''',
                              (num, origin, dest, dep_time, arr_time))

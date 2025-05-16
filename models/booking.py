from datetime import datetime

class Booking:
    def __init__(self, db):
        self.db = db

    def create(self, pid, fid):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.execute_query('''INSERT INTO Bookings (passenger_id, flight_id, booking_date)
                                 VALUES (?, ?, ?)''', (pid, fid, now))

import sqlite3

class DatabaseManager:
    def __init__(self, db_name="airline.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Flights (
            id INTEGER PRIMARY KEY,
            flight_number TEXT,
            origin TEXT,
            destination TEXT,
            departure_time TEXT,
            arrival_time TEXT
        )''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Passengers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            passport_number TEXT,
            nationality TEXT
        )''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Bookings (
            id INTEGER PRIMARY KEY,
            passenger_id INTEGER,
            flight_id INTEGER,
            booking_date TEXT,
            FOREIGN KEY(passenger_id) REFERENCES Passengers(id),
            FOREIGN KEY(flight_id) REFERENCES Flights(id)
        )''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Crew (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT
        )''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS CrewAssignments (
            id INTEGER PRIMARY KEY,
            crew_id INTEGER,
            flight_id INTEGER,
            FOREIGN KEY(crew_id) REFERENCES Crew(id),
            FOREIGN KEY(flight_id) REFERENCES Flights(id)
        )''')

        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur

    def close(self):
        self.conn.close()

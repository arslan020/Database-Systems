class Passenger:
    def __init__(self, db):
        self.db = db

    def add(self, name, passport, nation):
        self.db.execute_query('''INSERT INTO Passengers (name, passport_number, nationality)
                                 VALUES (?, ?, ?)''', (name, passport, nation))

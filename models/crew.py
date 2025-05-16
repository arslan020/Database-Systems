class Crew:
    def __init__(self, db):
        self.db = db

    def add(self, name, role):
        self.db.execute_query('''INSERT INTO Crew (name, role) VALUES (?, ?)''', (name, role))

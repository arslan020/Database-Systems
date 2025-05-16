class CrewAssignment:
    def __init__(self, db):
        self.db = db

    def assign(self, cid, fid):
        self.db.execute_query('''INSERT INTO CrewAssignments (crew_id, flight_id) VALUES (?, ?)''', (cid, fid))

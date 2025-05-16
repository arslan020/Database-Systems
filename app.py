from db_manager import DatabaseManager
from models.flight import Flight
from models.passenger import Passenger
from models.booking import Booking
from models.crew import Crew
from models.crew_assignment import CrewAssignment

def main():
    db = DatabaseManager()
    flight = Flight(db)
    passenger = Passenger(db)
    booking = Booking(db)
    crew = Crew(db)
    assign = CrewAssignment(db)

    while True:
        print("\n--- Airline Reservation System Menu ---")
        print("1. Add Flight")
        print("2. Add Passenger")
        print("3. Create Booking")
        print("4. Add Crew Member")
        print("5. Assign Crew to Flight")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            num = input("Flight Number: ")
            origin = input("Origin: ")
            dest = input("Destination: ")
            dep = input("Departure Time (YYYY-MM-DD HH:MM): ")
            arr = input("Arrival Time (YYYY-MM-DD HH:MM): ")
            flight.add(num, origin, dest, dep, arr)

        elif choice == '2':
            name = input("Name: ")
            passport = input("Passport Number: ")
            nation = input("Nationality: ")
            passenger.add(name, passport, nation)

        elif choice == '3':
            pid = int(input("Passenger ID: "))
            fid = int(input("Flight ID: "))
            booking.create(pid, fid)

        elif choice == '4':
            name = input("Crew Name: ")
            role = input("Role: ")
            crew.add(name, role)

        elif choice == '5':
            cid = int(input("Crew ID: "))
            fid = int(input("Flight ID: "))
            assign.assign(cid, fid)

        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

    db.close()

if __name__ == "__main__":
    main()

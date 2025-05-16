# Airline Reservation System

A simple terminal-based application to manage flights, passengers, bookings, crew members, and crew assignments using SQLite.

## Features

- Add flights with departure and arrival details  
- Add passengers with passport and nationality info  
- Create bookings linking passengers to flights  
- Add crew members with specific roles  
- Assign crew members to flights  

## Project Structure
airline_system/
├── db_manager.py           # SQLite database management and table creation
├── models/
│   ├── __init__.py
│   ├── flight.py           # Flight entity logic
│   ├── passenger.py        # Passenger entity logic
│   ├── booking.py          # Booking entity logic
│   ├── crew.py             # Crew member logic
│   └── crew_assignment.py  # Crew assignment logic
├── app.py                  # Main application file with CLI menu
├── requirements.txt        # Project dependencies (none external)
└── README.md               # This file

## Requirements

- Python 3.7+
- No external dependencies required (uses standard library sqlite3 and datetime)

## How to Run

Clone the repository or download the code files.

Open terminal in the project directory.

Run the app:
```bash
python app.py
```

## Usage
On running, the app shows a menu with options:

Add Flight

Add Passenger

Create Booking

Add Crew Member

Assign Crew to Flight

Exit

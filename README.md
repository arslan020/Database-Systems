# Student Course Management System

A simple terminal-based application to manage students, courses, and enrollments using SQLite and SQLAlchemy.

## Features

- Add students with unique emails  
- Add courses with unique names  
- Enroll students in courses  
- View all enrollments  

## Project Structure
student-course-management/
├── database/
│   ├── __init__.py
│   ├── models.py    
│   ├── sqlite_db.py     
├── business/
│   ├── __init__.py
│   ├── logic.py  
├── data_access/
│   ├── __init__.py
│   ├── crud.py     
└── main.py

## Requirements

- Python 3.7+
- Install dependencies:
  ```bash
  pip install sqlalchemy
  pip install sqlite3
    ```

## How to Run
Clone the repository or download the code files.

Open terminal in the project directory.

Run the app:
  ```bash
python main.py
```
## Usage
On running, the app shows a menu:
Options:
1. Add Student
2. Add Course
3. Enroll Student
4. View Enrollments
5. Exit

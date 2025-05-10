from database.models import Student, Course, Enrollment
from database.sqlite_db import Session
from sqlalchemy.exc import IntegrityError

def add_student(name, email):
    session = Session()
    student = Student(name=name, email=email)
    try:
        session.add(student)
        session.commit()
    except IntegrityError:
        print("Email already exists!")
        session.rollback()
    finally:
        session.close()

def add_course(name, description):
    session = Session()
    course = Course(name=name, description=description)
    try:
        session.add(course)
        session.commit()
    except IntegrityError:
        print("Course already exists!")
        session.rollback()
    finally:
        session.close()

def enroll_student(student_id, course_id):
    session = Session()
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    session.add(enrollment)
    session.commit()
    session.close()

def list_students():
    session = Session()
    students = session.query(Student).order_by(Student.name).all()
    session.close()
    return students

def list_courses():
    session = Session()
    courses = session.query(Course).all()
    session.close()
    return courses

def list_enrollments_grouped():
    session = Session()
    enrollments = (
        session.query(Student.name.label('student_name'), Course.name.label('course_name'))
        .join(Enrollment, Student.id == Enrollment.student_id)
        .join(Course, Course.id == Enrollment.course_id)
        .order_by(Student.name)
        .all()
    )
    session.close()
    return enrollments


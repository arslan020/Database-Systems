from data_access import crud

def register_student(name, email):
    crud.add_student(name, email)

def create_course(name, description):
    crud.add_course(name, description)

def enroll(name, course_name):
    students = crud.list_students()
    courses = crud.list_courses()
    student = next((s for s in students if s.name == name), None)
    course = next((c for c in courses if c.name == course_name), None)
    if student and course:
        crud.enroll_student(student.id, course.id)
    else:
        print("Student or Course not found.")

def view_enrollments():
    return crud.list_enrollments_grouped()

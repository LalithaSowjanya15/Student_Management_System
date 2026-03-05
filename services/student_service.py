from database.db import students

def add_student(name, roll_no):
    students.insert_one({
        "name": name,
        "roll_no": roll_no,
        "marks": {},
        "attendance": []
    })

def remove_student(roll_no):
    students.delete_one({"roll_no": roll_no})

def get_all_students():
    return list(students.find())

def get_student(roll_no):
    return students.find_one({"roll_no": roll_no})


def get_attendance_by_roll(roll_no):
    student = students.find_one({"roll_no": roll_no})
    if student:
        return student.get("attendance", [])
    return []


def student_exists(roll_no):
    student = students.find_one({"roll_no": roll_no})
    return student is not None

def get_student_by_roll(roll_no):
    return students.find_one(
        {"roll_no": roll_no},
        {"_id": 0}
    )
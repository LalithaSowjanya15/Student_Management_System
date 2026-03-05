from database.db import students

attendance_stack = []   # STACK

def mark_attendance(roll_no, status):

    students.update_one(
        {"roll_no": roll_no},
        {"$push": {"attendance": status}}
    )

    attendance_stack.append(roll_no)


def undo_attendance_by_roll(roll_no):

    # Check last attendance belongs to this roll number
    if attendance_stack and attendance_stack[-1] == roll_no:

        attendance_stack.pop()

        students.update_one(
            {"roll_no": roll_no},
            {"$pop": {"attendance": 1}}
        )

        return True

    return False

from database.db import students

def add_marks(roll_no, s1, s2, s3, s4, s5):

    total = s1 + s2 + s3 + s4 + s5
    percentage = total / 5

    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    else:
        grade = "C"

    students.update_one(
        {"roll_no": roll_no},
        {"$set": {
            "marks": {
                "subject1": s1,
                "subject2": s2,
                "subject3": s3,
                "subject4": s4,
                "subject5": s5
            },
            "percentage": percentage,
            "grade": grade
        }}
    )

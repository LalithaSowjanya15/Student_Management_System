from database.db import students

def add_relationship(r1, r2):

    students.update_one(
        {"roll_no": r1},
        {"$addToSet": {"relationships": r2}}
    )

    students.update_one(
        {"roll_no": r2},
        {"$addToSet": {"relationships": r1}}
    )


def get_relationships(roll_no):
    student = students.find_one({"roll_no": roll_no})
    if student and "relationships" in student:
        return student["relationships"]
    return []


def get_relationship_details(roll_no):
    student = students.find_one({"roll_no": roll_no})

    friends = []

    if student and "relationships" in student:
        for friend_roll in student["relationships"]:
            friend = students.find_one({"roll_no": friend_roll})
            if friend:
                friends.append({
                    "roll_no": friend_roll,
                    "name": friend["name"]
                })

    return friends
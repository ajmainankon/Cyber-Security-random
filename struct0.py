


students = []

for i in range(3):
    name = input(" NAME:  ")
    dorm = input(" DORM:  ")

    student = {"name": name, "dorm": dorm}
    
    students.append(student)

for student in students:
    print(f"{student['name']} is in this {student['dorm']}")
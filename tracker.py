def average(marks):
    if not marks:
        return 0.0
    return sum(marks)/len(marks)

def student_average(student):
    return average(student["marks"])

def rank(students):
    return sorted(students, key = student_average, reverse = True )

class_list =[
    {"name": "Asha" , "marks": [80, 90, 70]},
    {"name": "Sunita", "marks": [95, 85, 80]},
    {"name": "Arnab", "marks": [60, 70, 65]},
]

for position, student in enumerate(rank(class_list), start = 1):
    print(position, student["name"], round(student_average(student), 1))
import argparse
import csv

def average(marks):
    if not marks:
        return 0.0
    return sum(marks)/len(marks)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_marks(self,mark):
        if not 0 <= mark <= 100:
            raise ValueError("Marks should be between 0- 100")
        self.marks.append(mark)

    def get_average(self):
        return average(self.marks)

    def __repr__(self):
        return f"Student({self.name!r}, Average = {self.get_average():.1f})"


def student_average(student):
    return student.get_average()

def rank(students):
    return sorted(students, key = student_average, reverse = True )



def load_students(path):
    students = []
    with open(path, newline ="")as f:
        for row in csv.DictReader(f):
            marks = [int(m) for m in row["marks"].split()]
            students.append(Student(row["name"], marks))
    return students
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Show the class ranking.")
    parser.add_argument("csv_file", help = "path to marks CSV")
    args = parser.parse_args()


    students = load_students(args.csv_file)
    for position, student in enumerate(rank(students), start = 1):
        print(position, student.name, round(student_average(student), 1))







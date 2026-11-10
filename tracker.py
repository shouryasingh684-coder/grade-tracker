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
            raise ValueError("Marks should be between 1- 100")
        self.marks.append(mark)

    def get_average(self):
        return average(self.marks)

    def __repr__(self):
        return f"Student({self.name!r}, Average ={self.get_average():.1f})"


def student_average(student):
    return student.get_average()

def rank(students):
    return sorted(students, key = student_average, reverse = True )


if __name__ == "__main__":
    class_list =[
        Student("Asha", [80,90,70]),
        Student("Sunaina", [95,89,90]),
        Student("Arnab", [79,87,67]),

]

    for position, student in enumerate(rank(class_list), start = 1):
        print(position, student.name, round(student_average(student), 1))






from tracker import Student

def test_average_of_three_marks():
    s = Student("Asha",[80,90,70])
    assert s.get_average() == 80
def test_average_with_no_marks():
    s = Student("Ravi", [])
    assert s.get_average() == 0
def test_student_with_one_mark():
    s = Student("Nikhil",[75])
    assert s.get_average() == 25


 
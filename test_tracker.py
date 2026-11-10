import pytest
from tracker import Student, load_students
import csv

def test_average_of_three_marks():
    s = Student("Asha",[80,90,70])
    assert s.get_average() == 80
def test_average_with_no_marks():
    s = Student("Ravi", [])
    assert s.get_average() == 0
def test_student_with_one_mark():
    s = Student("Nikhil",[75])
    assert s.get_average() == 75

def test_student_with_zero_marks():
    s = Student("Jisha", [93,0,0])
    assert s.get_average() == 31

def test_unusual_marks():
    s = Student("Nikita", [90])
    with pytest.raises(ValueError):
        s.add_marks(150)

def test_repr():
    s = Student("Asha", [80, 90, 70])
    assert repr(s) == "Student('Asha', Average = 80.0)"

def test_load_student_reads_csv(tmp_path):
    f = tmp_path / "marks.csv"
    f.write_text("name,marks\nAsha,80 90 70\n")
    students = load_students(f)
    assert students[0].name == "Asha"
    assert students[0].marks == [80, 90, 70]

def test_load_students_reject_test_marks(tmp_path):
    f = tmp_path / "bad.csv"
    f.write_text("name,marks\nAsha,80 abc 70\n")
    with pytest.raises(ValueError):
        load_students(f)

    
    


 
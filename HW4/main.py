from student import Student
from student_data import StudentData
from database import Database

if __name__ == "__main__":
    db = Database()
    db.create_table()

    s1 = Student("Horodetska Alisa", "ІСД-32", "2001-26-10", "Kyiv")
    subjects = ["Math", "Programming", "English"]
    grades = [80, 95, 88]
    desired_grades = [90, 100, 95]

    data = StudentData(s1, subjects, grades, desired_grades).get_summary()
    db.insert_student(data)

    for row in db.fetch_all():
        print(row)

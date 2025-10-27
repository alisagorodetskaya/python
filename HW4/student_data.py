from desired_performance import DesiredPerformance
from student import Student
from performance import Performance

class RealPerformance(Performance):
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentData:
    def __init__(self, student, subjects, grades, desired_grades):
        self.student = student
        self.real_perf = RealPerformance(subjects, grades)
        self.desired_perf = DesiredPerformance(subjects, grades, desired_grades)

    def get_summary(self):
        return {
            "name": self.student.get_full_name(),
            "group": self.student.get_group_number(),
            "birth_date": self.student.get_birth_date(),
            "address": self.student.get_address(),
            "subjects": self.real_perf.subjects,
            "real_avg": self.real_perf.average_grade(),
            "desired_avg": self.desired_perf.average_grade()
        }

from performance import Performance

class DesiredPerformance(Performance):
    def __init__(self, subjects, grades, desired_grades):
        super().__init__(subjects, grades)
        self.desired_grades = desired_grades

    def average_grade(self):
        if len(self.desired_grades) == 0:
            return 0
        return sum(self.desired_grades) / len(self.desired_grades)

from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects, grades):
        self.subjects = subjects
        self.grades = grades

    @abstractmethod
    def average_grade(self):
        pass

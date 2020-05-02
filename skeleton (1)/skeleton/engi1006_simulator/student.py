from .person import Person
from .utilities import skillToGrade


class Student(Person):
    def __init__(self, name, skill):
        super(Student, self).__init__(name)
        self.grades = []
        self.skill = skill

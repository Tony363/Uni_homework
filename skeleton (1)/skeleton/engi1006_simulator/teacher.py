from .person import Person



class Teacher(Person):
    def __init__(self, name):
        super(Teacher, self).__init__(name)
        self.pay = 0

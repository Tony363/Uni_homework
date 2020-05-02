class Assignment(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.grades = []

    def __repr__(self):
        return "\tAssignment Difficulty: {}\n\tStudent Count:{}".format(self.difficulty, len(self.grades))

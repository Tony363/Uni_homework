from statistics import mean
import matplotlib.pyplot as plt

from .student import Student
from .assignment import Assignment
from .utilities import skillToGrade

class Course(object):
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []
        self.assignments = []
        self.grades = []
        self.names = []

    def __add__(self, other):
        if isinstance(other, Student):
            self.register(other)
        if isinstance(other, Assignment):
            self.assign(other)
        return self


    def register(self,Student):
        """
        simple register method that appends student object to courses student list 
        and appends student's name courses name list
        """
        self.students.append(Student)
        self.names.append(Student.name)
        

    def assign(self,Assignment):
        """
        takes in Assignment object and appends it to assignments list
        """
        self.assignments.append(Assignment)
        
        
    def student_grade(self,assignment):
        temp = []
        #iterate through each student object in course's students list.
        for student in self.students:
            #grade by taking iterations student skill with the assignment difficulty.
            grade = skillToGrade(student.skill,assignment.difficulty)
            #append grade to student objects grades list
            student.grades.append(grade)
            #append to assignment objects grades list
            assignment.grades.append(grade)
            # append to temp list array
            temp.append(grade)
        # append average grades to courses grades list
        self.grades.append(sum(temp)/len(temp))
        
    
            
        
    def __repr__(self):
        ret = '\n'
        ret += '\tProfessor: {}\n'.format(self.teacher)
        ret += '\tNumber of Students: {}\n'.format(len(self.students))

        if len(self.students):
            ret += '\t\t' + ','.join(str(s) for s in self.students) + '\n'

        ret += '\tNumber of Assignments: {}\n'.format(len(self.assignments))

        if len(self.assignments):
            ret += '\t\t' + ','.join(str(a.difficulty) for a in self.assignments) + '\n'

        if len(self.assignments) > 0:
            ret += 'Average grade: {}'.format(sum(self.grades) / len(self.grades))
        return ret

    def finish(self):
        # print average of all grades
        print(f'Class Average: {mean(self.grades)}')
        # print teacher pay
        print(f'Teacher pay: {self.teacher.pay}')

    def plot(self):
        fig, axes = plt.subplots(3, 1)
        axes[0].set_title('Grades by assignment')
        axes[0].set_ylabel('Grade')

        handles = []
       
        for s in self.students:
            # array initially empty
            handles.append(axes[0].scatter(list(range(len(self.assignments))), s.grades))

        # set legend
        axes[0].legend(handles, [s.name for s in self.students], loc='upper right', bbox_to_anchor=(1.35, 1), fancybox=True)

        # set x axis labels and ticks
        axes[0].set_xticks([i for i in range(len(self.assignments))])

        # next subplot
        axes[1].set_title('Grades by Student')
        axes[1].set_ylabel('Grade')

        handles = []
        for a in self.assignments:
            # array initially empty
            handles.append(axes[1].scatter(list(range(len(self.names))), a.grades))

        # set legend
        axes[1].legend(handles, [i for i in range(len(self.assignments))], loc='upper right', bbox_to_anchor=(1.3, 1), fancybox=True)

        # set x axis labels and ticks
        axes[1].set_xticks([i for i in range(len(self.students))])
        axes[1].set_xticklabels([s.name for s in self.students])

        # next subplot

        axes[2].set_title('Assignment Difficulty')
        axes[2].set_ylabel('Difficulty')

        difficulties = [a.difficulty for a in self.assignments]
        axes[2].plot(list(range(len(self.assignments))), difficulties)

        # set x axis labels and ticks
        axes[2].set_xticks([i for i in range(len(self.assignments))])

        # plot
        plt.subplots_adjust(right=.7, hspace=1)
        plt.show()
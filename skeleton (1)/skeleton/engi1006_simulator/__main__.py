from random import randint
from .teacher import Teacher
from .course import Course
from .student import Student
from .assignment import Assignment
from .utilities import printOpener, getTeacherName



def main():
    printOpener()

    # instantiate a teacher
    t = Teacher(getTeacherName())

    # instantiate a class
    c = Course(t)

    print("Course created!")
    print("Course Overview: {}".format(c))

    # register three student objects
    while input("Would you like to register students? (y/n)") == "y":
        print("Generating a new student...")

        skill = randint(0, 20) * 5
        student = Student(input("What would you like to name the new student: "), skill)
       
        c = c + student

        print("Registered new student: {}".format(student))
        print("Course Overview: {}".format(c))

    while input("Would you like to create assignments? (y/n)") == "y":
        print("Generating a new assignment...")
        assignment = Assignment(int(input("How difficult would you like the new assignment to be? (0-100):")))
 
        c = c + assignment

        print("Assigned new assignment: {}".format(assignment))
        
        # for each added assignment, we then grade each student in the course with the assignment
        c.student_grade(assignment)
        print("Course Overview: {}".format(c))


    print("Finishing the course...")

    # summarize the class
    c.finish()

    print("Course Overview: {}".format(c))
    
  
    
    if input("Plot? (y/n)") == "y":
        # plot the three charts
        c.plot()

if __name__ == '__main__':
    main()

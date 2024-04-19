#Calculate Student Marks in this App
# Single Responsibility Principle---> Each class/method has a single responsibility.
# Open/Closed Principle --->  Adding a new student result in it  doesn't require modifying existing code.
# Interface Segregation --->  Principle: There is no single interface forced upon all items.
# Liskov Substitution Principle --->  All Derived classes like Marks, Student MArks can be substituted for base class.
print("\n**************************************************************\n")
print("\n***********Welcome Hemant Student Result Calculation App******\n")
print("\n**************************************************************\n")

from abc import ABC, abstractmethod



# Marks Parent Class and its inherited from abstract class
class Marks(ABC):
    @abstractmethod
    def insertsubjectmarks(self, subject, mark):
        pass

    @abstractmethod
    def studenttotalmarks(self):
        pass

# Try to calculate of a student's marks
class StudentMarks(Marks):
    def __init__(self, name):
        self.name = name
        self.subject_marks = {}

    def insertsubjectmarks(self, subject, mark):
        self.subject_marks[subject] = mark

    def studenttotalmarks(self):
        return sum(self.subject_marks.values())

# Used main function here
if __name__ == "__main__":
    # Create three students here 
    students = [StudentMarks("Hemant"), StudentMarks("Hema"), StudentMarks("Hemann")]
    subjects = ["Python", "Java", "SoftwareDevelopment"]

    # below mentioned code in marks are input in the program
    for student in students:
        print(f"Enter marks for {student.name}==>")
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}==> "))
            student.insertsubjectmarks(subject, mark)

    # try to print total marks for each student
    print("\nTotal Marks for all students is = >")
    for student in students:
        total_marks = student.studenttotalmarks()
        print(f"{student.name}: {total_marks}")


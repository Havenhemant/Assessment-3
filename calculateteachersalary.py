#Calculate Salary of Hemant College Teacher
# Single Responsibility Principle---> Each class/method has a single responsibility in Calculate Salary App.
# Open/Closed Principle --->  Adding a new teacher salary in it  doesn't require modifying existing code of Calculate Salary App.
# Interface Segregation --->  Principle: There is no single interface forced upon all items.
# Liskov Substitution Principle --->  All Derived classes like Basic Pay College Teacher class can be substituted for base class.
print("\n**************************************************************\n")
print("\n***********Welcome to Teacher Salary Calculator******\n")
print("\n**************************************************************\n")
from abc import ABC, abstractmethod

# Implement College teacher Class from abstract main class
class CollegeTeacher(ABC):
    @abstractmethod
    def calculatesalary(self):
        pass

# Implement Basic Pay of College Teacher class from college Teacher class
class BasicPayCollegeTeacher(CollegeTeacher):
    def __init__(self, basicsalary, experienceyears, dapercentage, tapercentage):
        self.basicsalary = basicsalary
        self.experienceyears = experienceyears
        self.dapercentage = dapercentage
        self.tapercentage = tapercentage

    def calculatesalary(self):
        # Try to calculate Basic salary + DA + TA + experience bonus
        experiencebonus = self.experienceyears * 1000  
        da = self.dapercentage * self.basicsalary / 100
        ta = self.tapercentage * self.basicsalary / 100
        totalsalary = self.basicsalary + da + ta + experiencebonus
        return totalsalary

# Main function
if __name__ == "__main__":
    basicsalary = float(input("Enter basic salary my respected teacher==> "))
    experienceyears = int(input("Enter years of experience in teaching field ==> "))
    dapercentage = float(input("Enter Dearness Allowance percentage ==> "))
    tapercentage = float(input("Enter Travel Allowance percentage ==> "))
    teacher = BasicPayCollegeTeacher(basicsalary, experienceyears, dapercentage, tapercentage)
    totalsalary = teacher.calculatesalary()
    print(f"Total salary of the respected teacher ==> ${totalsalary}")

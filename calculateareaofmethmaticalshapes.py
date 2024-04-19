#calculate the area of various mathematical shapes
# Single Responsibility Principle---> Each class/method has a single responsibility.
# Open/Closed Principle --->  Adding a new Rectangle and square Shape Values in it  doesn't require modifying existing code.
# Interface Segregation --->  Principle: There is no single interface forced upon all items.
# Liskov Substitution Principle --->  All Derived classes like Shape, Rectangle, Square can be substituted for base class.
print("\n**************************************************************\n")
print("\n***********Welcome to mathematical shapes area calculator******\n")
print("\n**************************************************************\n")

from abc import ABC, abstractmethod

# Try to Shape class inherited from Abstract class
class Shape(ABC):
    @abstractmethod
    def calculateshapearea(self):
        pass

# Run rectangle area class that is inherited from shape class
class Rectanglearea(Shape):
    #constructor Function
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateshapearea(self):
        return self.length * self.width

# Run square area class that is inherited from shape class
class Squarearea(Shape):
    def __init__(self, side):
        self.side = side

    def calculateshapearea(self):
        return self.side ** 2

# Try to create Function to calculate area
def calculateshapearea(shape):
    return shape.calculateshapearea()

if __name__ == "__main__":
    # Try to input length and breadth of rectangle
    length = float(input("Enter length of rectangle ===> "))
    print("\n**************************************************************\n")
    width = float(input("Enter width of rectangle ===> "))
    print("\n**************************************************************\n")
    
    # Try to input side length of square
    side = float(input("Enter side length of square ===> "))
    print("\n**************************************************************\n")

    # Try to create rectangle and square class objects
    rectangle = Rectanglearea(length, width)
    square = Squarearea(side)

    # In Last Calculate and print area
    print("Area of rectangle ===> ", calculateshapearea(rectangle))
    print("Area of square ===> ", calculateshapearea(square))

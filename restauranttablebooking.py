# Restaurant Table Booking App
# Single Responsibility Principle---> Each class/method has a single responsibility.
# Open/Closed Principle --->  Adding a new customer deatils for restaurant table in it  doesn't require modifying existing code.
# Interface Segregation --->  Principle: There is no single interface forced upon all items.
# Liskov Substitution Principle --->  All Derived classes like Table, Restaurant table, Customer, Restaurant Customer, Restaurant Booking Manager can be substituted for base class.


#import abstract class and datetime class
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Create Table Class that is inherited from abstract class
class Table(ABC):
    @abstractmethod
    def istableavailable(self, tablebookingtime):
        pass

    @abstractmethod
    def addtablebooking(self, tablebookingtime, customerdetails):
        pass

# Create Restaurant Table Class that is inherited from table class
class RestaurantTable(Table):
    def __init__(self, restauranttablenumber):
        self.restauranttablenumber = restauranttablenumber
        self.bookings = []

    def istableavailable(self, tablebookingtime):
        for booking in self.bookings:
            if booking['time'] == tablebookingtime:
                return False
        return True

    def addtablebooking(self, tablebookingtime, customerdetails):
        self.bookings.append({'time': tablebookingtime, 'customerdetails': customerdetails})


# Create customer Table Class that is inherited from abstract class
class Customer(ABC):
    @abstractmethod
    def fetchdetails(self):
        pass

# Create restaurant customer Table Class that is inherited from customer class
class RestaurantCustomer(Customer):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def fetchdetails(self):
        return {'name': self.name, 'email': self.email, 'phone': self.phone}

# Create booking manager Class that is inherited from abstract class
class BookingManager(ABC):
    @abstractmethod
    def Bookrestauranttable(self, table, tablebookingtime, customer):
        pass

# Try to run booking manager
class RestaurantBookingManager(BookingManager):
    def Bookrestauranttable(self, table, tablebookingtime, customer):
        if table.istableavailable(tablebookingtime):
            customerdetails = customer.fetchdetails()
            table.addtablebooking(tablebookingtime, customerdetails)
            print(f"Table {table.restauranttablenumber} booked for {customerdetails['name']} at {tablebookingtime}")
            print("Thanku for Choosing Hemant Restaurant")
        else:
            print(f"Table {table.restauranttablenumber} is not available at {tablebookingtime}")

if __name__ == "__main__":
    # Try to built Table with numbers
    table1 = RestaurantTable(1)
    table2 = RestaurantTable(2)
    print("\n**************************************************************\n")
    print("\n***********Welcome to Hemant Restaurant Table booking App******\n")
    print("\n**************************************************************\n")
    print("\n*************Dear Customer Fill below mentioned Details********\n")
    # Take user input for customer details
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    tablebookingtimestr = input("Enter booking date and time (YYYY-MM-DD HH:MM): ")
    tablebookingtime = datetime.strptime(tablebookingtimestr, "%Y-%m-%d %H:%M")

    customer = RestaurantCustomer(name, email, phone)

   
    bookingmanager = RestaurantBookingManager()

    restauranttablenumber = int(input("Enter table number to book (1,2) ===> "))
    if restauranttablenumber == 1:
        bookingmanager.Bookrestauranttable(table1, tablebookingtime, customer)
    elif restauranttablenumber == 2:
        bookingmanager.Bookrestauranttable(table2, tablebookingtime, customer)
    else:
        print("Invalid table number")

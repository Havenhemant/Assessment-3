# Grocery shop 


# Single Responsibility Principle---> Each class/method has a single responsibility.
# Open/Closed Principle --->  Adding a new fruit item in it  doesn't require modifying existing code.
# Interface Segregation --->  Principle: There is no single interface forced upon all items.
# Liskov Substitution Principle --->  Derived classes can be substituted for base class.

# Create the abstract class
from abc import ABC, abstractmethod

# Item is the main class but inherited from abstract class 
class Item(ABC):
    @abstractmethod
    def getpricefunc(self):
        pass

# Constructor function used with apple inherited class for price calculation
class Apple(Item):
    def __init__(self, priceperunit):
        self.priceperunit = priceperunit
    
    def getpricefunc(self, quantity):
        return self.priceperunit * quantity

# Try to implement Constructor function used with banana inherited class for price calculation
class Banana(Item):
    def __init__(self, priceperunit):
        self.priceperunit = priceperunit
    
    def getpricefunc(self, quantity):
        return self.priceperunit * quantity

# Try to implement Constructor function used with Orange inherited class for price calculation
class Orange(Item):
    def __init__(self, priceperunit):
        self.priceperunit = priceperunit
    
    def getpricefunc(self, quantity):
        return self.priceperunit * quantity

# Try to implement Constructor function used with Shopping Cart inherited class for price calculation
class ShoppingCart:
    def __init__(self):
        self.items = []

    def addfruititem(self, item, quantity):
        self.items.append((item, quantity))

    def fruittotalprice(self):
        total_price = 0
        for item, quantity in self.items:
            total_price += item.getpricefunc(quantity)
        return total_price

# Rate per Item Declartion
if __name__ == "__main__":
    # Create items
    apple = Apple(priceperunit=1.5)
    banana = Banana(priceperunit=0.5)
    orange = Orange(priceperunit=2.0)
    
    # Create shopping cart object
    cart = ShoppingCart()
    
    # Add fruit items to the cart based on user input
    print("\n************************************************\n")
    print("\nWelcome to the Hemant grocery shop\n")
    print("\n************************************************\n")
    for _ in range(3):  # Add three items
        fruitname = input("Enter now Chooose item name (apple/banana/orange):").lower()
        quantity = int(input("Enter the choosed item quantity: "))
        
        if fruitname == "apple":
            cart.addfruititem(apple, quantity)
        elif fruitname == "banana":
            cart.addfruititem(banana, quantity)
        elif fruitname == "orange":
            cart.addfruititem(orange, quantity)
        else:
            print("Invalid item name. Skipping this food item from the list")

    # Now in last Calculate and print total price
    total_price = cart.fruittotalprice()
    print("Total Price of all fruits =", total_price)

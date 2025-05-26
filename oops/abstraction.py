### What is abstraction in OOPS?
# Abstraction is a concept in OOPS that hides unnecessary details from the user and only shows the essential features of a object.
# It allows us to focus on what an object does rather than how it does it.
# In Abstraction , there is a class that serves as a blueprint for other classes we cannot create objects directly from an abstract class.


# Decorator - that defines method in the abstract class but does not provide their implementation.
# To use abstraction python abc module (base class) is typically used

### Example 1 
from abc import ABC , abstractmethod
#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass #abstract method no implementation
# Concrete class for Circle
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2* 3.14 * self.radius

# Using the classes
circle = Circle(5)
print("Circle Area: ",circle.area())
print("Circle Perimeter: ",circle.perimeter())
        




from abc import ABC , abstractmethod
# Abstract class
class Payment(ABC):
    @abstractmethod 
    def make_payment(self , amount):
        pass
#Concrete class for  Credit Card Payment
class CreditCardPayment(Payment):
    def make_payment(self , amount):
        return f"Credit Card payment of ${amount} processed."
        
class PayPalPayment(Payment):
    def make_payment(self,amount):
        return f"PayPal amount of ${amount} processed."
# Using the classes
payment1 = CreditCardPayment()
print(payment1.make_payment(100))

payment2 = PayPalPayment()
print(payment2.make_payment(500))
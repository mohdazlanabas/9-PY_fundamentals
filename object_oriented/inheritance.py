# have certain attribute as defined in a base class
# base class, new class with inheritance and new functionality

class User:
    def log(self):
        print(self)

class Customer (User): #link User to Customer
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
    
    @property # decorator
    def name(self):
        return self._name # ._ means private
                            # data behind the scene
    
    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        print("Calculaitng Cost")
        self.membership = new_membership

    def __str__(self):
        return self.name + " " + self.membership

    def print_all(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        return False

customers = [
    Customer("Caleb", "Gold"),
    Customer("Brad", "Bronze"),
]

Customer.print_all(customers)
customers[0].log()
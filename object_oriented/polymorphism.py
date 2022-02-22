# to treat two class as same but treat them differently 

class User:
    def log(self):
        print(self)
        
class Teacher(User):
    def log(self):
        print("I am a teacher")

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

users = [ #customers
    Customer("John", "Platinum"),
    Customer("Caleb", "Gold"),
    Customer("Tim", "Silver"),
    Customer("Brad", "Bronze"),
    Teacher()
]
'''
Customer.print_all(customers)
customers[4].log()
'''

for user in users:
    user.log()
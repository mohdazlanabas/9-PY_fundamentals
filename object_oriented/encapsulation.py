# Hide inner details of class and data
# Only share whats needed
# Access through getters and setters
# encapsultion class, getter class, setter class

# create property
# property is like attribute
# property has extra layer (via @) to abstract the variable using method

class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
    
    @property # decorator
    def name(self):
        print('Getting Mame')
        return self._name # ._ means private
                            # data behind the scene
    
    @name.setter
    def name(self, name):
        print('Setting Mame')
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

__hash__ = None


Customer.print_all(customers)
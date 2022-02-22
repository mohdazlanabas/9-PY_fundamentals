class Customer:  # class
    def __init__(
        self, name, membership
    ):  # method(#parameters) --init-- constructor/initializer
        self.name = name
        self.membership = membership

    def update_membership(self, new_membership):
        print("Calculaitng Cost")
        self.membership = new_membership
        # Invoke API, Update Database

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership

    def print_all(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        return False

# __repr__ == __str__

"""
print("Customer Created")
c1 = customer("Caleb", "Gold") #(arguments, arguments)
c2 = customer("Brad", "Bronze")
print(c1.name, c1.membership)
print(c2.name, c2.membership)
"""

customers = [
    Customer("Caleb", "Gold"),
    Customer("Brad", "Bronze"),
]

"""
print(customer[1])
customer[1].update_membership("Silver")
print(customer[1])
"""

Customer.print_all(customers)
print(customers[0] == customers[1])
print(id(customers[0]), id(customers[1]))

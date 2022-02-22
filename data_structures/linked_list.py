class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

# Link first Node to second Node
list.headval.nextval = e2

# Link second node to third node
e2.nextval = e3

list.listprint()

# list.AtBegining
# list.AtEnd
# list.Inbetween

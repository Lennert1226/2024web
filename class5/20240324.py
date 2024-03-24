#Right traverse the linked list.
def rTraverse(head):
    print("Start right traverse!")
    ptr = head
    while ptr != None:
        print("The color of the car is {}.".format(ptr.color))
        ptr = ptr.next
    print("Finish right traverse!")
#Left traverse the linked list.
def lTraverse(head):
    print("Start left traverse!")
    ptr = head
    while ptr.next != None:
        ptr = ptr.next
    while ptr != None:
        print("The color of the car is {}.".format(ptr.color))
        ptr = ptr.previous
    print("Finish left traverse!")


#建立雙向串列，需斥定一個類別(Class)
class Car:
    def __init__(self, color):
        self.color = color
        self.previous = None
        self.next = None
#Initiate the first element fo the double linked list.
head = Car("red")
ptr = head
ptr.previous = None
ptr.next = None
#向後新增節點
new = Car("blue")
ptr.next = new
new.previous = ptr
ptr = new

rTraverse(head)
lTraverse(head)
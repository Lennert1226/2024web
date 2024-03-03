# 需自訂一個類別(Class)
class Car:

    def __init__(self, color):
        self.color = color
        self.next = None

def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next==head:
            break
        ptr = ptr.next
    print("Finsh traverse!")

#Initiate the first element of the linked list.
head = Car("red") #Add new element.
ptr = head #Set the position of the pointer.
ptr.next = None #There is no next element now.

new_data = Car("blue")
ptr.next = new_data
new_data.next = head
ptr = new_data

traverse(head)
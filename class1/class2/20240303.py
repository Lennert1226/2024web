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

new = Car("black")
new.next = head

ptr = head
while ptr.next != head:
    ptr = ptr.next
ptr.next = new

head = new

#將新結點X插入單向串列中間的位置
new = Car("pink")
new.next = head.next.next
head.next.next = new

ptr = head
while ptr.next != head:
    ptr = ptr.next
head = head.next
ptr.next = head

#刪除環狀串列的中間項
ptr = head
while ptr.next.color != "pink":
    ptr = ptr.next

ptr.next = ptr.next.next


traverse(head)
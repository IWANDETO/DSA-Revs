#!/usr/bin/python3

# This program illustrates searching an element in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addLast(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode

        else:
            lastNode = self.head

            while lastNode.next != None:
                lastNode = lastNode.next

            lastNode.next = newNode

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def printList(self):
        print("The Elements in the Linked List are: ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = Linkedlist()

    llist.addLast(10)
    llist.addLast(30)
    llist.addLast(20)

    print("Searching for Element 100")
    if llist.search(100):
        print("Search Found")
    else:
        print("Search Not Found")

    print("Searching for Element 30")
    if llist.search(30):
        print("Search Found")
    else:
        print("Search Not Found")

    

    llist.printList()
    
    

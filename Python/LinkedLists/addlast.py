#!/usr/bin/python3

# This program illustrates add an element at the end of a Linked List

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

    def printList(self):
        print("The Elements in the Linked List are: ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = Linkedlist()

    print("Adding element 10 to the list: ")
    llist.addLast(10)

    print("Adding element 30 to the list: ")
    llist.addLast(30)

    print("Adding element 20 to the list: ")
    llist.addLast(20)

    llist.printList()


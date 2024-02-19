#!/usr/bin/python3

# This program illustrates adding a Node at the beginning of a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addFirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        print("The Elements in the Linked List are: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = Linkedlist()

    print("Adding element 10 to the list:")
    llist.addFirst(10)

    print("Adding element 20 to the list:")
    llist.addFirst(20)

    print("Adding element 30 to the list:")
    llist.addFirst(30)

    llist.printList()
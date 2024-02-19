#!/usr/bin/python3

# This is a basic demonstration of a Linked List in Python

# First create a Class that initializes a Node Object
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

# Create a class to hold the Node Objects
class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        print("The Elements in the Linked List are: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        

if __name__ == "__main__":
    llist = Linkedlist()

    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    llist.head.next = middle
    middle.next = last
    

    llist.printlist()

        
        

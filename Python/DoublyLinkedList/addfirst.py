#!/usr/bin/python3

# This program illustrates adding a new node to the beginning of a Double Linked List

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addfirst(self, val):
        newNode = Node(val)

        if self.head == None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def printlist(self):
        temp = self.head
        print("The Elements in the list are:")
        while temp:
            print(temp.data)
            temp = temp.next
        

if __name__ == "__main__":
    llist = DoublyLinkedList()

    print("Adding Element 30 to the list")
    llist.addfirst(30)

    print("Adding Element 20 to the list")
    llist.addfirst(20)
    
    print("Adding Element 10 to the list")
    llist.addfirst(10)

    llist.printlist()
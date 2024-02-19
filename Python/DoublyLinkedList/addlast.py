#!/usr/bin/python3

# This program illustrates adding a node at the end of a Doubly Linked List

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addlast(self, val):
        newNode = Node(val)

        if self.head == None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode

        else:
            last = self.head

            while last.next != None:
                last = last.next

            last.next = newNode
            newNode.prev = last

    def printlist(self):
        temp = self.head
        print("Forward Traversal")
        while temp:
            print(temp.data)
            if temp.next == None:
                last = temp

            temp = temp.next

        print("Backward Traversal")
        temp = last
        while temp:
            print(temp.data)
            temp = temp.prev


if __name__ == "__main__":
    llist = DoublyLinkedList()

    print("Adding Element 10 to the List:")
    llist.addlast(10)

    print("Adding Element 20 to the List:")
    llist.addlast(20)

    print("Adding Element 30 to the List:")
    llist.addlast(30)

    llist.printlist()

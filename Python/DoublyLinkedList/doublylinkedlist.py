#!/usr/bin/python3

# This Program illustrates the basic functioning of a Doubly Linked List

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):       
        temp = self.head
        print("Forward Traversal") 
        while temp != None:
            print(temp.data, end=" ")
            if temp.next == None:
                last = temp
            temp = temp.next

        print("Backward Traversal")
        temp = last
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.prev

if __name__ == "__main__":
    llist = DoublyLinkedList()

    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    llist.head.next = middle
    middle.prev = llist.head
    middle.next = last
    last.prev = middle

    llist.printlist()
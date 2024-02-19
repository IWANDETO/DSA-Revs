#!/usr/bin/python3

# This program illustrates deleting a Node in a Doubly Linked List

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

    def delete(self, key):

        if self.head == None:
            print("List is empty")
            return
        
        temp = self.head

        while temp != None and temp.data != key:
            temp = temp.next
        
        if temp == None:
            print("Key Not Found")

        elif temp == self.head:
            self.head = self.head.next
            self.head.prev = None
        
        elif temp.next == None:
            temp.prev.next = None

        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


    
if __name__ == "__main__":
    llist = DoublyLinkedList()

    llist.addlast(10)
    llist.addlast(20)
    llist.addlast(30)
    llist.addlast(40)

    print("The Elements in the list before deletion are: ")
    llist.printlist()

    key = 50
    print("Deleting Element: ", key)
    llist.delete(key)

    llist.printlist()




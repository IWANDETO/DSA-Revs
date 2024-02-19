#!/usr/bin/python3

# This program ilustrates deleting a Node Object in a Linked List

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
        
    def printlist(self):
        temp = self.head
        print("The Elements in the List are: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next

        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next

if __name__ == "__main__":
    llist = Linkedlist()
    
    llist.addLast(10)
    llist.addLast(20)
    llist.addLast(30)
    llist.addLast(40)

    llist.printlist()

    print("Deleting element 30 in the list:")
    llist.delete(30)

    llist.printlist()


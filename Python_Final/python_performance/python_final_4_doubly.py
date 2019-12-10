"""
4. Doubly Linked Lists
    Implement a reverse function by using the doubly linked list below. Do this 
    without using the tail node. 

#******************************************************
    class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    class DoublyLinkedList:
        def __init__(self):
            self.head = None

        # Two cases, empty list and list with items
        def append(self, data):
            newNode = Node(data)
            if self.head is None:
                newNode.prev = None
                self.head = newNode            
            else:
                probe = self.head
                while probe.next != None:
                    probe = probe.next
                newNode.prev = probe
                probe.next = newNode

        def print_list(self):
            probe = self.head
            while probe != None:
                print(probe.data)
                probe = probe.next

        def insert_node(self, index, data):
            probe = self.head
            while probe != None:
                if probe.next is None and probe.data == index:
                    self.prepend(data)
                elif probe.next == index:
                    newNode = Node(data)
                    prev = probe.prev
                    prev.next = newNode
                    newNode.next = probe
                    newNode.prev = prev
                probe = probe.next

        def reverse(self):
            # implement this function

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append("A")
    doubly_linked_list.append("b")
    doubly_linked_list.append([7,245,8,68,"hello"])
    doubly_linked_list.insert_node(1, "one")
    doubly_linked_list.print_list()
    doubly_linked_list.reverse()
    doubly_linked_list.print_list()
#******************************************************
"""

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Two cases, empty list and list with items
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.prev = None
            self.head = newNode            
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            newNode.prev = probe
            probe.next = newNode

    def print_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # had to modify this to make it work
    def insert_node(self, index, data):
        probe = self.head
        while probe != None:
            if probe.next is None and index >= 1:
                # changed from prepend to append
                self.append(data)
            elif index == 0:
                newNode = Node(data)
                # get previous node
                prev = probe.prev
                # make next point to new node (A -> 'one')
                prev.next = newNode
                # make new node next point to probe ('one' -> b)
                newNode.next = probe
                # make new node prev point to previous node ('one' -> A)
                newNode.prev = prev
                # make probe prev point to new node (b -> 'one')
                probe.prev = newNode
            probe = probe.next
            index -= 1
    # function that reverses the order of the doubly linked list
    def reverse(self):
        ## find last node
        # set probe to head node
        probe = self.head
        #print(probe.data)
        # loop until probe is the last node
        while True:
            if probe.next == None:
                break
            else:
                probe = probe.next
        # set head to probe
        self.head = probe
        ## start working backward
        # loop until the beginning is reached
        while probe is not None:
            # set temp to the probe's next node
            temp = probe.next
            # set the probe's next node to the probe's previous node
            probe.next = probe.prev
            # set the probe's previous node to the probe's original next node
            probe.prev = temp
            # move probe to the next node
            probe = probe.next

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("A")
doubly_linked_list.append("b")
doubly_linked_list.append([7,245,8,68,"hello"])
doubly_linked_list.insert_node(1, "one")
doubly_linked_list.print_list()
doubly_linked_list.reverse()
doubly_linked_list.print_list()
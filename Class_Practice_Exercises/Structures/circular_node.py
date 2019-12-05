"""
Circular Linked List - Special case of singly linked list.
                        Insertion and removal of the first node are special cases of the insert ith
                        and remove ith operations on a singly linked list. 
                        These are special because the head pointer must be reset.
                        You can use circular linked lists with a dummy header node.
                        Contains a link from the last node back to the first node in the strucure.
"""
from node import Node

class CircularLinked:
    # initialize linked list with head and tail attributes set to none
    def __init__(self):
        self.head = None
        self.tail = None
    
    # append Nodes to linked list
    def append(self, data):
        # initialize a new Node
        newNode = Node(data)
        # if the linked list is empty
        if not self.head:
            # set the head to a new Node
            self.head = newNode
            # set the tail to the head
            self.tail = self.head
            # link the next attribute to itself to form the circle
            self.head.next = self.head
        # if the linked list is not empty
        else:
            # create the link from the current tail Node to the new Node using "next" attribute
            self.tail.next = newNode
            # set the new tail Node as the current tail Node's next Node
            self.tail = self.tail.next
            # create the link back to the head using the "next" attribute
            newNode.next = self.head

    # prepend Nodes to linked list
    def prepend(self, data):
        # instantiate a new Node object
        newNode = Node(data)
        # set the newNode's "next" attribute to the head
        newNode.next = self.head
        # set the location of head to the new Node
        self.head = newNode

    # printing our linked list
    def print_linked_list(self):
        # instantiate probe pointer at the head
        probe = self.head
        # loop and print each Node's data until the last Node is reached
        while probe != self.tail:
            print(probe.data)
            probe = probe.next
        # print the final Node's data
        print(probe.data)
    

circ_linked_list = CircularLinked()
circ_linked_list.append('happy')
circ_linked_list.prepend('sad')
circ_linked_list.print_linked_list()
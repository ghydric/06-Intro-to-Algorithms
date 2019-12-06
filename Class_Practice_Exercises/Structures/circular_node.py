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
    
    def get_length(self):
        # initiate probe pointer
        probe = self.head
        # initiate length variable
        length = 0
        # loop through each Node in linked list and add 1 to length each iteration
        while probe != self.tail:
            length += 1
            probe = probe.next
        # add 1 more to length for tail Node
        length += 1
        return length

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

    # insert Node at a specific index location in linked list
    def insert_node(self, index, data):
        # is linked list empty or index less than zero
        if self.head is None or index <= 0:
            # instantiate a newNode and set head to it
            self.head = Node(data, self.head)
            self.tail = self.head
        # if index is greater than or equal to the length of the linked list
        elif index >= self.get_length():
            # create the link from the current tail Node to the new Node with
            # the new Node's next attribute being the head
            self.tail.next = Node(data, self.head)
            # set tail to new Node
            self.tail = self.tail.next
        # find our position to insert
        else:
            # instantiate our probe pointer
            probe = self.head
            # loop while index is greater than 1 and the probe's next Node is not the head Node
            while index > 1 and probe.next != self.head:
                probe = probe.next
                index -= 1
            # create the link to the new Node and the new Node's next Node
            probe.next = Node(data, probe.next)

    # remove a Node at a specific location
    def delete_node(self, index):
        # is this the only node?
        if self.head.next is self.head:
            # grab the data from the Node being removed
            removedItem = self.head.data
            # set head and tail to None
            self.head = None
            self.tail = self.head
        # if index is less than or equal to zero
        elif index <= 0:
            # grab the data from the Node being removed
            removedItem = self.head.data
            # make the current head's next Node the new head Node
            self.head = self.head.next
            # skip the old head Node and create link from current tail Node to new head Node
            self.tail.next = self.head
        else:
            # initialize probe pointer
            probe = self.head
            # while there are nodes to loop through
            while index > 1 and probe.next.next != self.head:
                # set probe to next node
                probe = probe.next
                # decrement index by one
                index -= 1
            # set the removed item to the data of the probe's next Node
            removedItem = probe.next.data
            # if probe's next node is the current tail Node
            if probe.next.data == self.tail.data:
                # set the probe as the new tail Node
                self.tail = probe
                # skip the removed Node and create the next link to the head Node
                probe.next = self.head
            else:
                # skip the removed Node and create the next link to the following Node
                probe.next = probe.next.next
        # return the removed item
        return removedItem

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
circ_linked_list.append('third')
circ_linked_list.prepend('first')
circ_linked_list.insert_node(1, "second")
circ_linked_list.insert_node(6, "last")
print(f"The removed node is: {circ_linked_list.delete_node(0)}")
print(f"The head node is: {circ_linked_list.head.data}")
print(f"The tail node is: {circ_linked_list.tail.data}")
print(f"The tail's next node is: {circ_linked_list.tail.next.data}")
circ_linked_list.print_linked_list()
print(circ_linked_list.get_length())
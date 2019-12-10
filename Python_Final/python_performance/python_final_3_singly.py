"""
3. Singly Linked Lists
    Implement an insert_before() and insert_after() function for singly linked lists.
    insert_before takes in an index as an argument and inserts the node before the given
        index. (Its possible we already did this in class...)
    insert_after takes in an index as an argument and inserts the node after the given
        index.
"""

# This class will represent a singly linked node
class Node:
    def __init__(self, data, next = None):
        # Instantiates a Node with a default next of none
        self.data = data
        self.next = next

# This LinkedList class will instantiate Node objects and we'll
# add methods to this class to add functionality
class LinkedList:
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

    # add things to our linked list
    def append(self, data):
        # instantiate a new Node
        newNode = Node(data)
        # is there something in our linked list yet
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        # there are node(s) in our linked list
        else:
            # initialize our probe pointer
            probe = self.head
            # is probe at the end of the linked list
            while probe.next != None:
                probe = probe.next
            # set the linked list's final Node's "next" attribute to the newly created Node
            probe.next = newNode
            # set the tail node to the newly added node
            self.tail = newNode

    # insert Nodes into specific location in linked list
    def insert_before(self, index, data):
        # is linked list empty or index less than zero
        if self.head is None or index <= 0:
            # instantiate a newNode then set head and tail to it
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
            # loop while there are Nodes to loop through
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # add the new Node
            probe.next = Node(data, probe.next)

    # insert Nodes into specific location in linked list
    def insert_after(self, index, data):
        # add 1 to the index to account for inserting node after the supplied index
        index += 1
        # is linked list empty or index less than zero
        if self.head is None or index <= 0:
            # instantiate a newNode then set head and tail to it
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
            # loop while there are Nodes to loop through
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # add the new Node
            probe.next = Node(data, probe.next)

    # printing our linked list
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

# create a linked list
linked_list = LinkedList()
# append items to linked list
linked_list.append("I'm, first!")
linked_list.append("Hello, I'm the second Node.")
# insert_before
linked_list.insert_before(1, "Insert before index 1 (should be second)")
# insert_after
linked_list.insert_after(1, "Insert after index 1 (should be third)")
# print linked_list
linked_list.print_linked_list()
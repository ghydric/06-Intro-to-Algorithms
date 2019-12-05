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

    # add things to our linked list
    def append(self, data):
        # instantiate a new Node
        newNode = Node(data)
        # is there something in our linked list yet
        if self.head is None:
            self.head = newNode
        # there are node(s) in our linked list
        else:
            # initialize our probe pointer
            probe = self.head
            # is probe at the end of the linked list
            while probe.next != None:
                probe = probe.next
            # set the linked list's final Node's "next" attribute to the newly created Node
            probe.next = newNode

    # prepend Nodes to linked list
    def prepend(self, data):
        # instantiate a new Node object
        newNode = Node(data)
        # set the newNode's "next" attribute to the head
        newNode.next = self.head
        # set the location of head to the new Node
        self.head = newNode

    # insert Nodes into specific location in linked list
    def insert_node(self, index, data):
        # is linked list empty or index less than zero
        if self.head is None or index <= 0:
            # instantiate a newNode and set head to it
            self.head = Node(data, self.head)
        # find our position to insert
        else:
            # instantiate our probe pointer
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(data, probe.next)

    # remove a Node at a specific location
    def delete_node(self, index):
        # is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            # initialize probe pointer
            probe = self.head
            # while there are nodes to loop through
            while index > 1 and probe.next.next != None:
                # set probe to next node
                probe = probe.next
                # decrement index by one
                index -= 1
            # set the removed item to the 
            removedItem = probe.next.data
            # 
            probe.next = probe.next.next
        # return the removed item
        return removedItem

    # printing our linked list
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
"""
# create a linked list
linked_list = LinkedList()
# append items to linked list
linked_list.append("A")
linked_list.append("Hello, I'm the second Node.")
# prepend items to linked list
linked_list.prepend("I should be at the beginning")
linked_list.prepend("Now I'm first")
# insert items to linked list
linked_list.insert_node(2, "inserted")
linked_list.insert_node(24, "next insert")
# remove node
linked_list.delete_node(1)
# print the linked list
linked_list.print_linked_list()
"""

"""
# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node('A', None)
node3 = Node('B', node2)

# print(node3.data)
"""
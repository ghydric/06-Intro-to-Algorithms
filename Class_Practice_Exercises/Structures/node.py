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

    # remove a Node at a specific location
    def delete_node(self, index):
        # if length of linked list is zero (no Nodes)
        if self.get_length() == 0:
            return "There are no Nodes in this list."
        # if only one node is in linked list
        elif self.head.next is None:
            # grab the data from the Node being removed
            removedItem = self.head.data
            # set head and tail Nodes to None
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
            while index > 1 and probe.next.next != None:
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
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

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
#linked_list.delete_node(1)
# testing links
print(f"The removed node is: {linked_list.delete_node(0)}")
print(f"The head node is: {linked_list.head.data}")
print(f"The tail node is: {linked_list.tail.data}")
print(f"The tail's next node is: {linked_list.tail.next.data}")
# print the linked list
linked_list.print_linked_list()


"""
# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node('A', None)
node3 = Node('B', node2)

# print(node3.data)
"""
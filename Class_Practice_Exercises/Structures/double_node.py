"""
Doubly Linked Lists - very similar to singly linked, however these have
                      prev pointer and a tail node.
                      Move left, to a previous node, from a given node
                      move immediately to the last node.
"""

# create double node class
class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

# create doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # add nodes to the end of linked list (two cases to consider)
    def append(self, data):
        # initialize new node
        newNode = DoubleNode(data)
        # if linked list is empty (case 1)
        if self.head is None:
            # set head and tail to the new Node
            self.head = newNode
            self.tail = self.head
        # if linkedlist is not empty (case 2)
        else:
            # create the link from the current tail Node to the new Node using "next" attribute
            self.tail.next = newNode
            # create the link from the new Node back to the current tail Node using "prev" attribute
            newNode.prev = self.tail
            # set the new tail Node as the current tail Node's next Node
            self.tail = self.tail.next

    # add nodes to beginning of linked list (two cases to consider)
    def prepend(self, data):
        # initialize new node
        newNode = DoubleNode(data)
        # if linked list is empty (case 1)
        if self.head is None:
            # set head and tail to the new Node
            self.head = newNode
            self.tail = self.head
        # if linked list is not empty (case 2)
        else:
            # create the link from the new Node to the current head using "next" attribute
            newNode.next = self.head
            # create the link from the current head back to the new Node using "prev" attribute
            self.head.prev = newNode
            # set the head to the new Node
            self.head = newNode

    # insert Nodes at specific location in linked list
    def insert_node(self, index, data):
        # is linked list empty or index less than or equal to zero
        if self.head is None or index <= 0:
            # instantiate a new Node, then set head and tail to it
            self.head = DoubleNode(data, self.head)
            self.tail = self.head
        # find our position to insert
        else:
            # instantiate our probe pointer
            probe = self.head
            # while the last Node has not been reached, loop through linked list
            while index > 1 and probe.next != None:
                # move probe pointer
                probe = probe.next
                # decrement index by 1
                index -= 1
            # set the "next" attribute for probe to be a new Node
            probe.next = DoubleNode(data, probe.next, probe)

    # remove Nodes at specific location in linked list
    def remove_node_at(self, index):
        # is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            # initialize probe pointer
            probe = self.head
            # while there are nodes to loop through
            while index > 1 and probe.next.next != None:
                # set probe to next Node
                probe = probe.next
                # decrement index by one
                index -= 1
            # set the removed item to the probe's next Node's data
            removedItem = probe.next.data
            # re-establish the link to the probe's next Node by setting it to the Node following the next Node (skipping the next Node)
            probe.next = probe.next.next
            # re-establish the link back from the newly linked next Node to the current probe Node
            probe.next.prev = probe
        # return the removed item
        return removedItem

    # print linked list method
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

# create doubly_linked_list
doubly_linked_list = DoublyLinkedList()
# append Nodes
doubly_linked_list.append("first node's data")
doubly_linked_list.append([1,2, "howdy"])
# prepend Nodes
doubly_linked_list.prepend("now I'm first")
doubly_linked_list.prepend("nope, now I'm first")
# insert Nodes
doubly_linked_list.insert_node(2, "Inserted at index 2")
doubly_linked_list.insert_node(1, "Inserted at index 1")
# remove Nodes
doubly_linked_list.remove_node_at(3)
doubly_linked_list.remove_node_at(0)
# print out doubly_linked_list
doubly_linked_list.print_linked_list()



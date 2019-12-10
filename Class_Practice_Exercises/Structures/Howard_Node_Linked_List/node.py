class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    
    def __init__(self):
        # constructor
        self.head = None
    

    def prepend(self, data):
        # place a new node with given data at the start of the linked list
        self.head = Node(data, self.head)
    
    
    def append(self, data):
        # place a new node with given data at the end of the linked list
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)


    def insert(self, index, data):
        # place a new node with given data at the given index in the linked list
        if self.head is None or index == 0:
            self.prepend(data)
        else:
            curr = self.head
            while curr.next is not None and index > 1:
                curr = curr.next
                index -= 1
            curr.next = Node(data, curr.next)
            
    
    def find(self, key):
        # find the first index of the given key value within the linked list, returns -1 if not found
        curr = self.head
        index = 0
        while curr is not None and curr.data != key:
            curr = curr.next
            index += 1
        if curr is not None:
            return index
        return -1
    

    def remove(self, key):
        # removes the first node found with data that matches the given key value within the linked list
        if self.head.data == key:
            self.head = self.head.next
        else:
            curr = self.head
            while curr is not None and curr.data != key:
                prev = curr
                curr = curr.next
            if curr is not None:
                prev.next = curr.next
                curr.next = None
            else:
                print("Did not find an element with data", key)
    

    def remove_at(self, index):
        # removes the node from the linked list at the given index
        if index <= 0 or self.head.next is None:
            self.head = self.head.next
        else:
            curr = self.head
            while index > 1 and curr.next.next is not None:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next


    def replace(self, key, data):
        # finds the first node within the linked list that has data matching the given key
        # then replaces that data with the given data
        if self.head.data == key:
            self.head.data = data
        else:
            curr = self.head
            while curr is not None and curr.data != key:
                curr = curr.next
            if curr is not None:
                curr.data = data
            else:
                print("Did not find an element with data", key)


    def replace_at(self, index, data):
        # finds the node with the given index and replaces its data with the given data
        if self.head is None:
            print("Index out of range")
        elif index <= 0 or self.head.next is None:
            self.head.data = data
        else:
            curr = self.head
            while index > 0 and curr is not None:
                curr = curr.next
                index -= 1
            if curr is not None:
                curr.data = data
            else:
                print("Index out of range")


    def pop(self):
        # removes and returns the data of the last node in the linked list
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        removed_item = curr.next.data
        curr.next = None
        return removed_item


    def reverse(self):
        # reverses the order of the linked list
        curr = self.head
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def count(self, key):
        # returns an integer that is a count of the number of nodes with data matching the key value
        curr = self.head
        count = 0
        while curr is not None:
            if curr.data == key:
                count += 1
            curr = curr.next
        return count


    def copy(self):
        # returns a shallow copy of the linked list
        new_linked_list = SinglyLinkedList()
        curr = self.head
        while curr is not None:
            new_linked_list.append(curr.data)
            curr = curr.next
        return new_linked_list


    def clear(self):
        # removes all data from the linked list
        self.head = None


    def swap_nodes(self, index1, index2):
        # swaps nodes at the given indices
        curr = self.head
        while index1 > 0 and curr is not None:
            curr = curr.next
            index1 -= 1
        if curr is None:
            print("Index1 is out of range")
            return
        first_node = curr
        curr = self.head
        while index2 > 0 and curr is not None:
            curr = curr.next
            index2 -= 1
        if curr is None:
            print("Index2 is out of range")
            return
        second_node = curr
        temp = first_node.data
        first_node.data = second_node.data
        second_node.data = temp


    def __repr__(self):
        # returns a string of all the data in the nodes in the linked list
        nodes = []
        curr = self.head
        while curr is not None:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'


    def __len__(self):
        # returns an integer of a count of the number of nodes in the linked list
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            curr = self.head
            while (curr.next is not self.head):
                curr = curr.next
            curr.next = Node(data, self.head)
    
    def prepend(self, data):
        self.head = Node(data, self.head)
        if self.head.next is None:
            self.head.next = self.head
        else:
            curr = self.head.next
            while (curr.next is not self.head.next):
                curr = curr.next
            curr.next = self.head

    def insert(self, index, data):
        # place a new node with given data at the given index in the linked list
        if self.head is None or index == 0:
            self.prepend(data)
        else:
            curr = self.head
            while curr.next is not self.head and index > 1:
                curr = curr.next
                index -= 1
            curr.next = Node(data, curr.next)

    def remove_at(self, index):
        # removes the node from the linked list at the given index
        if index <= 0 or self.head.next is None:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            while index > 1 and curr.next.next is not self.head:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next
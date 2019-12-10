from node import SinglyLinkedList
import random

class Node:

    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList(SinglyLinkedList):

    def __init__(self):
        # constructor
        self.head = None
        self.tail = None


    def append(self, data):
        # place a new node with given data at the end of the linked list
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data, self.tail)
            self.tail = self.tail.next
    

    def prepend(self, data):
        # place a new node with given data at the start of the linked list
        self.head = Node(data, None, self.head)
        if self.head.next is not None:
            self.head.next.prev = self.head
        else:
            self.tail = self.head


    def insert(self, index, data):
        # place a new node with given data at the given index in the linked list
        if self.head is None or index == 0:
            self.head = Node(data, None, self.head)
            if self.tail is None:
                self.tail = self.head
            else:
                self.head.next.prev = self.head
        else:
            curr = self.head
            while index > 1 and curr is not self.tail:
                curr = curr.next
                index -= 1
            curr.next = Node(data, curr, curr.next)
            if curr is self.tail:
                self.tail = curr.next
            else:
                curr.next.next.prev = curr.next

                
    def remove(self, key):
        # removes the first node found with data that matches the given key value within the linked list
        if self.head.data == key:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        else:
            curr = self.head
            while curr is not None and curr.data != key:
                curr = curr.next
            if curr is not None:
                curr.prev.next = curr.next
                if curr is self.tail:
                    self.tail = curr.prev
                else:
                    curr.next.prev = curr.prev
            else:
                print("Did not find an element with data", key)
    

    def remove_at(self, index):
        # removes the node from the linked list at the given index
        if index <= 0 or self.head.next is None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        else:
            curr = self.head
            while index > 1 and curr.next is not self.tail:
                curr = curr.next
                index -= 1
            if curr.next is self.tail:
                self.tail = curr
            else:
                curr.next.next.prev = curr
            curr.next = curr.next.next


    def pop(self):
        # removes and returns the data of the last node in the linked list
        removed_item = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = self.tail
        else:
            self.tail.next = None
        return removed_item


    def clear(self):
        # removes all data from the linked list
        self.head = None
        self.tail = None


    def reverse(self):
        # reverses the order of the linked list
        curr = self.tail
        while curr is not None:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = curr.next
        temp = self.head
        self.head = self.tail
        self.tail = temp


    def copy(self):
        # returns a shallow copy of the linked list
        new_linked_list = super().copy()
        new_linked_list = DoublyLinkedList.make_double(new_linked_list)
        return new_linked_list


    def lazy_sort(self, reverse = False):
        # sorts the linked list
        new_list = []
        curr = self.head
        while curr is not None:
            new_list.append(curr.data)
            curr = curr.next
        new_list.sort(reverse = reverse)
        self.clear()
        for item in new_list:
            self.append(item)


    @staticmethod
    def make_double(single_linked_list):
        # static method to take a singly linked list and convert it into a doubly linked list
        new_linked_list = DoublyLinkedList()
        curr = single_linked_list.head
        while curr is not None:
            new_linked_list.append(curr.data)
            curr = curr.next
        return new_linked_list
"""
Python Basics Performance Exam

    This exam is open note, open book, and open internet. Feel free to use any resources
    you can (other than someone else) to solve the following problems. Direct collaboration with another
    individual will result in immediate failure and consequences to follow. If you are unsure about 
    whether or not you can use a resource please ask me. If you are unsure about any of the prompts I can 
    clarify. 

    Comments are necessary. 

    Each problem will weigh the same towards the final grade. 4 Problems at 25% each. 

    Please send each problem as a .py file separately. Please direct message them to me (Daniel Curran) 
    through slack. If there are supporting files for a problem then please send them with the .py file 
    as a zipped folder. 

    You will have 4 hours to complete this exam. If you complete this portion early and I have verified
    I have everything needed to grade your exam then you will be released.

    Happy Coding.


1. Recursion
    Have a user input a list of at least 5 integers. Write a function to find the 
    GCD (greatest common divisor) of two randomly selected numbers from the list by 
    using recursion. Output the answer to the terminal.

    The greatest common divisor of two or more integers, which are not all zero, is 
    the largest positive integer that divides each of the integers. For example, the 
    gcd of 8 and 12 is 4.

2. Sorting
    We discussed how to do a selection sort in class, the function is posted below.
    Modify the selectionSort function so it sorts in reverse order and call it
    reverseSort(). Don't use the list method reverse...

#******************************************************
    # The selectionSort function
    def selectionSort(my_list):
        i = 0
        # do n-1 searches for the smallest
        while i < len(my_list) -1:
            minIndex = i
            j = i + 1
            # start a search
            while j < len(my_list):
                if my_list[j] < my_list[minIndex]:
                    minIndex = j
                j += 1
            # Exchange if needed
            if minIndex != i:
                swap(my_list, minIndex, i)
            i += 1

    # The swap function
    def swap(my_list, i , j):
        # exchanges the positions of i and j 
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp

    my_list = [1,4,5,6,2,3,9]
    print(my_list)
    selectionSort(my_list)
    print(my_list)
#******************************************************

3. Singly Linked Lists
    Implement an insert_before() and insert_after() function for singly linked lists.
    insert_before takes in an index as an argument and inserts the node before the given
        index. (Its possible we already did this in class...)
    insert_after takes in an index as an argument and inserts the node after the given
        index.

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
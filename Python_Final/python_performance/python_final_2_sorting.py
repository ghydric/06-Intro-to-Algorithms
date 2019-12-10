"""
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
"""

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

# The reverseSort function
def reverseSort(my_list):
    i = 0
    # do n-1 searches for the smallest
    while i < len(my_list) -1:
        minIndex = i
        j = i + 1
        # start a search
        while j < len(my_list):
            if my_list[j] > my_list[minIndex]:
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
reverseSort(my_list)
print(my_list)
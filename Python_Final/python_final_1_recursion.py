"""
1. Recursion
    Have a user input a list of at least 5 integers. Write a function to find the 
    GCD (greatest common divisor) of two randomly selected numbers from the list by 
    using recursion. Output the answer to the terminal.

    The greatest common divisor of two or more integers, which are not all zero, is 
    the largest positive integer that divides each of the integers. For example, the 
    gcd of 8 and 12 is 4.
"""
from random import choices

# recursive gcd function returns the greatest common divisor between two integers
def rec_gcd(a,b):
    # if the remainder is 0, return a
    if(b==0):
        return a
    # recursively call itself with b and the remainder from dividing a by b
    else:
        return rec_gcd(b,a%b)

# function that prompts user to input five integers that will be stored in a list that gets returned
def get_int_list():
    # instantiate integer list
    int_list = []
    
    # loop gathering user input to add to list
    for i in range(1,6):
        int_list.append(int(input(f"Please enter an integer for list item #{i}: ")))
    
    # return the list
    return int_list

# main function
def main():
    # create the integer list
    my_list = get_int_list()

    # randomly choose two integers from the list
    random_ints = choices(my_list, k=2)

    # print out random ints for testing
    print(f'Random int 1: {random_ints[0]}')
    print(f'Random int 2: {random_ints[1]}')

    # find the gcd of the two chosen integers
    gcd = rec_gcd(random_ints[0], random_ints[1])

    # print out the gcd
    print(f"GCD is: {gcd}")

# call main function
main()
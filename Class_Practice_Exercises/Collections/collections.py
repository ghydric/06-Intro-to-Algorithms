"""
**************************** Collection Types ********************************

collection - a group of zero or more items that can be treated as a 
            conceptual unit. Things like strings, lists, tuples, and dictionaries.

            other types of collections include stacks, queues, priority queues,
            binary search trees, heaps, graphs, and bags.

linear collection - like people in a line, they are ordered by position
                    each item except the first has a unique predecessor

                    some examples include: grocery lists, stacks of dinner plates,
                    and a line at the ATM.

                    (Item 1) - (Item 2) - (Item 3) - (Item 4)

hiearchical collection - ordered in a structure resembling an upside-down tree.
                        Each data item except the one at the top (root) has just one
                        predecessor called its parent, but potentially has many
                        successors called children.

                        some examples include: a file directory system, a company's
                        organizational tree, and a book's table of contents.

graph collection - also called graph, each item can have many predecessors
                    and many successors. These are also called neighbors.

                    (Item 1) --- (Item 2)
                        |        /
                        |       /
                        |      /
                        (Item 3)


                    some examples include: airline routes between cities, electrical
                    wiring diagrams, and the world wide web.

unordered collections - these are not in any particular order, and it's not possible to 
                        meaningfully speak of an item's predecessor or successor.

                        an example includes a bag of marbles

**************************** Operation Types ********************************

Determine the size - Use Python's len() function to obtain the number of items
                    currently in the collection.

Test for item membership - Use Python's "in" operator to search for a given target
                            item in the collection. Returns True if the item is found
                            and False otherwise.

Traverse the collection - Use Python's "for loop" to visit each item in the collection.
                        The order which items are visited depends upon the type of collection.

Obtain a string representation - Use Python's str function to obtain the string representation
                                    of the collection.

Test for equality - Use Python's == operator to determine whether two collections are equal.
                    Two collections are equal if they are of the same type and contain the same
                    items. The order in which pairs of items are compared depends upon the type
                    of collection.

Concatenate two collections - Use Python's "+" operator to obtain a new collection of the same
                                type as the operands, and containing the items in the two operands.

Convert to another type of collection - Create a new collection with the same items as a source collection.

Insert an item - Add the item to the collection, possibly at a given position.

Remove an item - Remove the item from the collection, possibly at a given position.

Replace an item - Combine removal and insertion into one operation

Access or retrieve an item - Obtain an item, possibly at a given position.

"""
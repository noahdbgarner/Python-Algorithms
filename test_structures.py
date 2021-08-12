import random
from linked_lists.linked_list import *
from strings import *
from trees_and_graphs import *



class Structures:
    """
    A Representation of a structures class which will contain examples of all data structures used in
    Leetcode Algorithms with Python
    """
    def __init__(self):
        pass

    # Int list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 20, 10, 2, 3, 4, 5, 6, 11]

    # String list
    string_list = ["Internet", "Big", "Brady and Noah", "I wanna",
                 "clean up language"]

    # Some extremely long string
    long_string = "abdhfgeyrtwuiso :80594 means we are finding the index position of the character s[i] and adding 1 to obtain index position after the repeating element and :: gets the rest of the string that is f 's character after the repeating element. + s[i] denotes appending of s[i] to the string after removing repeated elements finally we are storing it to f"

    # Length 3 Linked List
    LL1 = LinkedList()
    LL1.insert(2)
    LL1.insert(4)
    LL1.insert(3)

    # Length 3 Linked List
    LL2 = LinkedList()
    LL2.insert(5)
    LL2.insert(6)
    LL2.insert(4)

    sum:int = 19
    print(int(sum/10))
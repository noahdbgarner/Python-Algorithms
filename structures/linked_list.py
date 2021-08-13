import random
class Node:
    """
    A representation of a Node of a Linked List with a random and position field for various algorithms
    """
    def __init__(self: object, data: int, position: int, next: 'Node' = None, rand: 'Node' = None):
        self.data = data
        self.next = next
        self.rand = rand
        self.position = position
#linked list implementation for testing. Contains insertion, add random pointers, and print
class LinkedList:
    """
    A representation of a LinkedList which includes insert, add rand pointer, and print methods.
    TBD: Additional methods for leetcode algorithms
    """
    def __init__(self, head: 'Node' = None, length: int = 0):
        #Head is not static!
        self.head = head
        self.length = length
        self.visitedDict = {}

    #Insert new nodes into a linked list starting with head
    def insert(self, data: int) -> 'Node':
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            # Let's a node know it's position in the list. This could be useful
            current.next = Node(data,self.length)
        else:
            self.head = Node(data, 0)
        # Python uses -= and += to decrement/increment values. This let's a linkedList track it's own length
        # Done insertin, increment the LL length
        self.length += 1

    def add_random_pointer_to_ll_nodes(self) -> None:
        current = self.head
        while current:
            #10% chance the current.rand Node will be Null
            if random.randint(0, 10) == 7:
                current.rand = None
            else:
                target = self.head
                for i in range(0, random.randint(1,self.length)):
                    current.rand = target
                    target = target.next
            current = current.next

    @staticmethod
    def print_ll(head) -> None:
        current = head
        while current:
            if current.rand is not None:
                print(f"Current Node: {current.position}", f"Rand Node: {current.rand.position}", f"Data: {current.data}")
                current = current.next
            else:
                print(f"Current Node: {current.position}", f"Rand Node: Null", f"Data: {current.data}")
                current = current.next


# Linked List length 3
LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(3)

# Linked List length 3
LL2 = LinkedList()
LL2.insert(5)
LL2.insert(6)
LL2.insert(4)

# Linked List with duplicate data
LLDuplicates = LinkedList()
LLDuplicates.insert(4)
LLDuplicates.insert(1)
LLDuplicates.insert(1)
LLDuplicates.insert(4)
LLDuplicates.insert(0)
LLDuplicates.insert(3)
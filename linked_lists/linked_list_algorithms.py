from linked_list import *
from test_structures import *
'''
Title: 
    Copy Linked List of Nodes with a Random Pointer: Inspired by "Copy Linked List"
Description:
    Given a generic linked list with a next pointer, and a random next pointer, construct a copy of said list
    Asking for a deep copy, which just means the new list has different references.
    Deep copies are more expensive and complicated (graph of references, yikes)
    Random pointer can point to another node or be null
'''
def copy_random_list(self, head) -> 'Node':
    if head is None:
        return None
    # If we have already processed the current node, then we simply return the cloned version of it.
    if head in self.visitedDict:
        return self.visitedDict[head]
    # create a new node
    # with the value same as old node.
    node = Node(head.data, head.position)
    # Save this value in the hash map. This is needed since there might be
    # loops during traversal due to randomness of random pointers and this would help us avoid them.
    self.visitedDict[head] = node
    # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
    # Thus we have two independent recursive calls.
    # Finally we update the next and random pointers for the new node created.
    node.next = self.copy_random_list(head.next)
    node.rand = self.copy_random_list(head.rand)

    return node



'''
Title: 
    Add Two Numbers Given Two non-empty Linked Lists
Description:
    Given two linked lists representing two non-negative integers, where each node contains 1 digit,
    Add the two numbers and return the sum as a linked list. A Node may be 0.. The last Node cannot be
    0, ie. No leading 0s. 
    eg. l1 = (2) -> (4) -> (3)      342
        l2 = (5) -> (6) -> (4)      465
        sum= (7) -> (0) -> (8)      807
        
Notes:
    The trick is handling the carry, and the digits are stored in reverse order
    Just like in regular addition, we start summing th least significant digits first, and
    move a carry over (1 or 0). 
    Keep in mind: 1 list longer than the other, one list is null or empty, and sum could have
    an extra carry at the very end
'''
def addTwoNumbers(l1: Node, l2: Node) -> Node:
        l3 = Node(0,0)
        dummy = l3
        carry = 0
        while l1 or l2 or (carry is 1):
            cursum = 0
            if l1 is not None:
                cursum += l1.data
                l1 = l1.next
            if l2 is not None:
                cursum += l2.data
                l2 = l2.next
            cursum += carry
            dummy.data = cursum % 10

            carry = 0
            if cursum > 9:
                carry = 1

            if l1 or l2 or (carry is 1):
                dummy.next = Node(0,0)
                dummy = dummy.next

        return l3



#Notes: You can view this problem like a graph... DUH!

if __name__ == "__main__":

    LL1 = Structures.LL1
    LL1.print_ll(LL1.head)
    LL2 = Structures.LL2
    LL1.print_ll(LL2.head)


    LL3 = LinkedList(length=3)
    LL3.print_ll(addTwoNumbers(LL1.head, LL2.head))
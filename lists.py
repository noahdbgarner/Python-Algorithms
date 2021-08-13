from structures.linked_list import *

def copy_list_with_random_pointer(head: 'Node') -> 'Node':
    """
    Description:
        Given a generic linked list with a next pointer, and a random next pointer, construct a copy of said list
        Asking for a deep copy, which just means the new list has different references.
        Deep copies are more expensive and complicated (graph of references, yikes)
        Random pointer can point to another node or be null

    Args:
        head (Node):

    Returns:
        node (Node): the head of the new list

    Explanation:
        You should view this problem as a graph

    Edge Cases:

    Complexity Analysis:

    """
    visitedDict = {}
    if head is None:
        return None
    # If we have already processed the current node, then we simply return the cloned version of it.
    if head in visitedDict:
        return visitedDict[head]
    # create a new node
    # with the value same as old node.
    node = Node(head.data, head.position)
    # Save this value in the hash map. This is needed since there might be
    # loops during traversal due to randomness of random pointers and this would help us avoid them.
    visitedDict[head] = node
    # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
    # Thus we have two independent recursive calls.
    # Finally we update the next and random pointers for the new node created.
    node.next = copy_list_with_random_pointer(head.next)
    node.rand = copy_list_with_random_pointer(head.rand)

    return node

def add_two_linked_lists(l1: 'Node', l2: 'Node') -> 'Node':
    """
    Description:
        Given two linked lists representing two non-negative integers, where each node contains 1 digit,
        Add the two numbers and return the sum as a linked list. A Node may be 0.. The last Node cannot be
        0, ie. No leading 0s.
        eg. l1 = (2) -> (4) -> (3)      342
            l2 = (5) -> (6) -> (4)      465
            sum= (7) -> (0) -> (8)      807

    Args:
        l1 (Node): the head of the first linked list
        l2 (Node): the head of the second linked list

    Returns:
        l3 (Node): the head of the new linked list

    Explanation:
        The trick is handling the carry, and the digits are stored in reverse order
        Just like in regular addition, we start summing the least significant digits first, and
        move a carry over (1 or 0).

    Edge Cases:
        1 list longer than the other
        one list is null or empty
        Extra carry at the very end of the list

    Complexity Analysis:
        Time: O(n) where n is the length of the list
        Space O(n) where n is the number of elements in the list
    """
    l3 = Node(0,0)
    dummy = l3
    carry = 0
    while l1 or l2 or (carry == 1):
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

        if l1 or l2 or (carry == 1):
            dummy.next = Node(0,0)
            dummy = dummy.next

    return l3


if __name__ == "__main__":

    list1 = LL1

    list2 = LL2

    newlist = add_two_linked_lists(list1.head, list2.head)
    LinkedList.print_ll(newlist)
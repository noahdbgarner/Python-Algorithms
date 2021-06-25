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



# TODO: Finish this algorithm
def addTwoNumbers(l1: Node, l2: Node) -> Node:
    carry = 0
    head = Node(0, 0)
    curr = head
    while l1 or l2 is not None:
        if (l1.data + l2.data + carry) >= 10:
            curr.data = (l1.data + l2.data + carry) % 10
            carry = 1
        else:
            curr.data = l1.data + l2.data + carry
            carry = 0
        if l1.next or l2.next is not None:
            curr.next = Node(0, 0)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        else:
            break
    return head



#Notes: You can view this problem like a graph... DUH!

if __name__ == "__main__":

    LL1 = Structures.LL1
    LinkedList.print_ll(head=LL1.head)
    LL2 = Structures.LL2
    LinkedList.print_ll(head=LL2.head)

    LL3 = addTwoNumbers(LL1.head, LL2.head)
    LinkedList.print_ll(LL3)
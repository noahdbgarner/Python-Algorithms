import random
#Remember to white board the problem first. If you are struggling, make sure to look at hints
class Node:
    def __init__(self: object, data: int, position: int, next: 'Node' = None, rand: 'Node' = None):
        self.data = data
        self.next = next
        self.rand = rand
        self.position = position
#linked list implementation for testing. Contains insertion, add random pointers, and print
class LinkedList:
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

    def print_ll(self, head) -> None:
        current = head
        print(f"Length: {self.length}")
        for i in range(0,self.length):
            if current.rand is not None:
                print(f"Current Node: {current.position}", f"Rand Node: {current.rand.position}", f"Data: {current.data}")
                current = current.next
            else:
                print(f"Current Node: {current.position}", f"Rand Node: Null", f"Data: {current.data}")
                current = current.next

    #Given a generic linked list with a next pointer, and a random next pointer, construct a copy of said list
    #Asking for a deep copy, which just means the new list has different references.
    #Deep copies are more expensive and complicated (graph of references, yikes)
    #Random pointer can point to another node or be null
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
#Notes: You can view this problem like a graph... DUH!

if __name__ == "__main__":

    LL = LinkedList()

    LL.insert(4)
    LL.insert(-1)
    LL.insert(0)
    LL.insert(2)

    LL.add_random_pointer_to_ll_nodes()
    LL.print_ll(LL.head)


    deepCopy = LL.copy_random_list(LL.head)
    LL.print_ll(deepCopy)
class LinkedNode:
    '''
    Implementation of a linked list in python without an explicit LinkedList class - only using LinkedNode objects.
    Enqueue, dequeue, and len() are methods defined on the head node of the linked list.

    Repr: LinkedNode(value)
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

    def enqueue(self, value):
        if self.next == None:
            self.next = LinkedNode(value)
        else:
            self.next.enqueue(value)

    def dequeue(self):
        value = self.value

        self.value = self.next.value
        self.next = self.next.next

        return value

    def __len__(self):
        c = 0
        a = self
        while a != None:
            c += 1
            a = a.next
        return c

    def __repr__(self):
        return f'LinkedNode({self.value})'


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def util(self, head):                           # Does most of the work
    curr = head
    tail = head
    while curr:                                 # Iterate through the list
        follow = curr.next
        kid = curr.child
        if kid:                                 # If child exists, find its tail
            kidTail = self.util(kid)
            kidTail.next = follow               # Connect child tail to main list
            if follow: follow.prev = kidTail
            curr.next = kid
            kid.prev = curr
            curr.child = None                   # Now, the child is no longer in a different branch
        else:
            curr = curr.next
        if curr:
            tail = curr
    return tail                                 # For child tail recursion. Not needed for main flattening

def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if head:
        self.util(head)
    return head
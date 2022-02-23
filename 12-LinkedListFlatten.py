class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return
    curr = head
    while curr:                         # This is iterative method
        if curr.child:                  # If child exists, flatten and extend
            kid = curr.child
            follow = curr.next
            curr.next = kid
            kid.prev = curr
            if follow:                  # If originally there were more elements, connect them to end of child list
                while kid.next:
                    kid = kid.next
                kid.next = follow
                follow.prev = kid
            curr.child = None           # Now, current node child is no longer a different branch
        curr = curr.next
    return head
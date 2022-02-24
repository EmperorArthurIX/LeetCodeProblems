class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return
    newhead = head                                      # Keeping track
    vis = {head: Node(head.val)}                        # Visited nodes
    while head:
        if head.next and head.next not in vis:
            vis[head.next] = Node(head.next.val)
        if head.random and head.random not in vis:
            vis[head.random] = Node(head.random.val)
        if head.next:
            vis[head].next = vis[head.next]
        if head.random:
            vis[head].random = vis[head.random]
        head = head.next
    return vis[newhead]
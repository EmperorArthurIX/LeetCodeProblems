def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Looks like 2 passes, but it is actually 1 pass, split into 2 parts
    """
    end = head
    remove = head
    dist = 0
    while dist < n:             # Condition: 1 <= n <= size
        end = end.next          # Establish distance n between head and end node
        dist += 1
    if end is None:             # if end is actually end, remove head
        remove = remove.next
        return remove
    while end is not None and end.next is not None:
        end = end.next          # if end is not last, move till it becomes last
        remove = remove.next    # remove node at established distance from last
    
    remove.next = remove.next.next      # remove node at established distance from last
    return head
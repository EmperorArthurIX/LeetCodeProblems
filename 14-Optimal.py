def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return
    if head and not head.next:
        return head
    if k == 0:
        return head                 # Time saving checks
    
    curr = head
    tail = None
    size = 0
    while curr:
        tail = curr
        curr = curr.next
        size += 1                   # Calculating size
    
    if k%size == 0:                 # Time saving
        return head
    
    tail.next = head                # Making cyclic to ease process
    
    curr = head
    for i in range(2*size - k%size - 1):    # Which Node will become TAIL after these many rotations
        curr = curr.next
    ans = curr.next                         # Mark Head
    curr.next = None                        # Un-Cycle the list
        
    return ans
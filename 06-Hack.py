def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    sentinel = ListNode(0)              # Make extra 'prev' pointer to avoid having to check 'leading nodes'
    sentinel.next = head
    prev, current = sentinel, head      # 2 pointer technique from here itself, instead of previous setup
    
    while current:                         
        if current.val == val:
            prev.next = current.next
        else:
            prev = prev.next
        
        current = current.next
    
    return sentinel.next                # Even though we made a new node, it is never returned!
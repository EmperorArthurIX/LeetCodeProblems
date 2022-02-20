def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    if not head or not head.next:               # Base Case
        return head
    
    new_head = self.reverseList(head.next)      # Recursive call
    
    head.next.next = head                       # Action after recursion - latest first, oldest last
    head.next = None
    
    return new_head
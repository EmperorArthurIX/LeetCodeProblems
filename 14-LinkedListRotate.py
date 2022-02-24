def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if head and not head.next:
            return head
        if k == 0:
            return head
        
        curr = head
        tail = None
        size = 0
        while curr:
            tail = curr
            curr = curr.next
            size += 1
        
        for i in range(k % size):
            curr = head
            while curr.next is not tail:    # Cheekiness is missing. Cyclic list would not need this
                curr = curr.next
            tail.next = head
            head = tail
            curr.next = None
            tail = curr
            
        return head
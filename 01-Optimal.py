def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:        # Safety condition
            return False
        slow = head
        fast = head.next        # Already crossed, or 'None'
        
        while slow != fast:     # Will run at least once, even if fast is 'None'
            if fast is None or fast.next is None:       # Check if list ended
                return False
            slow = slow.next
            fast = fast.next.next
        return True
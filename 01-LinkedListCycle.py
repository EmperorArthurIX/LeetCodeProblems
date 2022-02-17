def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:        # Safety case
            return False
        if head.next is None:   # Safety case - Only one node which does not loop to itself
            return False
        slow = head
        fast = head
        passcount = 0           # Count of how many times fast crosses slow
        while fast.next is not None and slow is not None and passcount <= 2:
            slow = slow.next
            fast = fast.next.next       # Moves twice as fast as slow
            if slow is fast:            # If they are same means fast looped back and came here
                passcount += 1
            if slow == None or fast == None:    # Check if reached end
                break
        if passcount >= 2:
            return True
        return False                    # If we reach here then no loop
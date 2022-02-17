def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:            # Safety case
            return None
        slow = head
        fast = head.next
        tracker = head              # Tracks position of loop if any
        if fast:                    # When only 2 elements
            if fast.next == tracker:
                return tracker
        while tracker is not None:      # Seems inefficient
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is tracker:         # Required condition
                return tracker
            if fast is slow:            # Move tracker once loop is found
                tracker = tracker.next
        return tracker
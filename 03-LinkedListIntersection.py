def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    aptr = headA
    bptr = headB
    while aptr is not None:             # Brute Force. Not feasible
        while bptr is not None:
            if aptr.val != bptr.val:    # Check entire B to 1 of A
                bptr.next
            else: return bptr
        bptr = headB                    # If pattern was not continous, restart for next A
        aptr.next
    return None
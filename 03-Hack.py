def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    ABSOLUTE HACK. NOTHING LESS.
    """
    aptr = headA
    bptr = headB
    alen = blen = 0
    while aptr is not bptr:         # Ends either when matched, or after LCM(m,n) iterations when both become None
        if not aptr:
            aptr = headB            # Exchange pointers if a list ends
        else: aptr = aptr.next
        if not bptr:
            bptr = headA            # Exchange here as well
        else: bptr = bptr.next
    return bptr                     # Depending on how above loop ended, it is either intersection or None
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    aptr = headA
    bptr = headB
    aset = set()                    # Space: O(m)
    while aptr is not None:         # Time: O(m + n)
        aset.add(aptr)
        aptr = aptr.next
    
    while bptr is not None:
        if bptr in aset:
            return bptr
        bptr = bptr.next
    
    return None
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aptr = headA
        bptr = headB
        alen = blen = 0
        while aptr is not None:
            alen += 1
        while bptr is not None:
            blen += 1
        diff = abs(alen - blen)
        
        aptr = headA
        bptr = headB
        if alen > blen:
            for i in range(diff):
                aptr = aptr.next
        else:
            for i in range(diff):
                bptr = bptr.next
        
        while aptr is not None and bptr is not None:
            if aptr is bptr:
                return aptr
            aptr = aptr.next
            bptr = bptr.next
        
        return None
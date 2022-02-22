def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode(-1)
    curr = result

    while l1 and l2:                                        # Till 1 of the lists finishes
        add = l1.val + l2.val                               # Find value
        if add >= 10:                                       # If double digit, do this:
            if curr.next:                                       # If the next node is already initialised with a carry over:
                curr.next.val += add%10                             # Add value%10 to the carry over
                if curr.next.val >= 10:                             # Check if this is now double digit
                    curr.next.val = curr.next.val%10                # If yes, then keep only the last digit
            else:                                               # If no:
                curr.next = ListNode(add%10)                        # Just add the last digit into a new node, and make it next
            curr.next.next = ListNode(1)                        # Add a new node after this, with carry over 1
        else:                                               # If no:
            if curr.next:                                       # If the next node is already initialised with a carry over:
                curr.next.val += add                                # Add value%10 to the carry over
                if curr.next.val >= 10:                             # Check if this is now double digit
                    curr.next.val = curr.next.val%10                # If yes, then keep only the last digit
                    curr.next.next = ListNode(1)                    # Add a new node after this, with carry over 1
            else:                                               # If no:
                curr.next = ListNode(add)                           # Just add the value to a new node, and make it next
        curr = curr.next
        l1 = l1.next
        l2 = l2.next
    
    # Do the same process as above for remaining elements, in case one list is larger
    while l1:
        if curr.next:
            curr.next.val += l1.val%10
            if curr.next.val >= 10:
                curr.next.val = curr.next.val%10
                curr.next.next = ListNode(1)
        else:
            curr.next = ListNode(l1.val)
        l1 = l1.next
        curr = curr.next
    while l2:
        if curr.next:
            curr.next.val += l2.val%10
            if curr.next.val >= 10:
                curr.next.val = curr.next.val%10
                curr.next.next = ListNode(1)
        else:
            curr.next = ListNode(l2.val)
        l2 = l2.next
        curr = curr.next
    
    return result.next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode(-1)
    curr = result
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        else:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
    while list1:                                # If anything left in list1, means list2 is empty
        curr.next = list1
        curr, list1 = curr.next, list1.next
    while list2:                                # If anything left in list2, means list1 is empty
        curr.next = list2
        curr, list2 = curr.next, list2.next
    
    return result.next
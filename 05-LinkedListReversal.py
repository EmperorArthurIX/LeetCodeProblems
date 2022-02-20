def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:           # Safety check
        return head
    curr = head
    newhead = head
    while head.next is not None:                    # Stopping condition
        curr = head.next                            # Move to next node
        if curr:
            head.next = curr.next                   # Point head to node after next
            curr.next = newhead                     # Point next node to head of reversed list
            newhead = curr                          # Re-assign the head of the reversed list
    return newhead
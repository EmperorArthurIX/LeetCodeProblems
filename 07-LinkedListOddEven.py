def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Group all odd indexed nodes together, and even indexed nodes together
    Head is 1, so odd
    """
    if not head or not head.next:                   # Safety check
        return head
    odd = head
    evenTail = head.next
    while evenTail:                                 # Till we reach end of list
        if evenTail.next:
            evenHead = odd.next                     # A node for where Even Group starts
            odd.next = evenTail.next                # Inserting the next odd between current even and odd
            evenTail.next = evenTail.next.next      # Grouping even, since odd was recently shifted
            odd.next.next = evenHead                # Pointing end of Odd to start of Even
        # Move forward
        odd = odd.next
        evenTail = evenTail.next
    return head
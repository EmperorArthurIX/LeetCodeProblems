def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:                    # Safety case
        return
    
    while head:                         # Removes all leading nodes containing 'val'
        if head.val == val:
            head = head.next
        else: break
    if not head or not head.next:       # If we reached end in previous step, return
        return head
    curr = head.next                    # 2 Pointer technique of removal from this point onwards
    prev = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = None
            curr = prev.next
            continue
        curr = curr.next
        prev = prev.next
    return head
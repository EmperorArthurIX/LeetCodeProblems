def reverseList(self, head: ListNode):
    if head is None or head.next is None:               # Safety check
        return head
    curr = head
    newhead = head
    while head.next is not None:
        curr = head.next
        if curr:
            head.next = curr.next                       # Refer next
            curr.next = newhead                         # Swap position
            newhead = curr                              # Assign new head
    return newhead
            
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    curr = head
    count = 0
    while curr:                                         # Inefficient. Stores length
        count += 1
        curr = curr.next
    curr = head
    for _ in range(count//2):                           # After storing length, moves to center
        curr = curr.next
    rev = self.reverseList(curr)                        # Reverses list
    curr = head
    while rev:
        if curr.val != rev.val:                         # Check Palindrome
            return False
        curr = curr.next
        rev = rev.next
    return True
def isPalindrome(self, head: ListNode) -> bool:
        rev = None                                      # Will be head of reverse list
        slow = fast = head
        while fast and fast.next:                       # Instead of length first and move later, this
            fast = fast.next.next
            rev,rev.next,slow = slow,rev,slow.next      # Beautiful assignments. Reversal of first half of list
        if fast:
            slow = slow.next                            # If odd length
        while rev and rev.val == slow.val:              # Checking Palindrome
            slow = slow.next
            rev = rev.next
            """
            Checks:
            List: 1,2,3,4,3,2,1
            slow: 3,2,1 (right half after middle)
            rev: 3,2,1 (reverse of first half)
            """
        return not rev                                  # Beautiful use of implicit conversion
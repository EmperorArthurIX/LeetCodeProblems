def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:       # Safety case
            return None
        walker, runner = head, head
        isCircular = False                          # Checks basic loop
        while runner.next and runner.next.next:     # Floyd Cycle Detection - '01-Optimal.py'
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                isCircular = True
                break
        if not isCircular:                          # If no loop, finish
            return None
        firstStep = head                            # Initiate index search
        while firstStep != walker:                  # Position searching
            firstStep = firstStep.next              # Move at same speed
            walker = walker.next
        return firstStep                            # When matched, return location
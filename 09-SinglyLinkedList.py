"""
Beautiful visualisation contributed by https://leetcode.com/Suraj1199
"""

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        # self.show("init")     #****

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            # self.show(f"get({index}) = {-1}")     #****
            return -1
        itr = self.head
        i = index
        while i > 0:
            itr = itr.next
            i -= 1
        # self.show(f"get({index}) = {itr.val}")    #****
        return itr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size +=1
        # self.show(f"addAtHead({val})")    #****

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
        self.size +=1
        # self.show(f"addAtTail({val})")    #****

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index > 0 and index < self.size:
            itr = self.head
            i = index - 1
            while i:
                itr = itr.next
                i -= 1
            node = ListNode(val)
            node.next = itr.next
            itr.next = node
            self.size +=1
        elif index == self.size:
            self.addAtTail(val)
        else:
            return
        # self.show(f"addAtIndex({index}, {val})")  #****

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            node = self.head
            self.head = node.next
            del node
        else:
            itr = self.head 
            i = index - 1
            while i:
                itr = itr.next
                i -= 1
            node = itr.next
            itr.next = node.next
            del node
        self.size -=1
        # self.show(f"deleteAtIndex({index})")     #****
    
    # # uncomment to get visualisation of solution
    # def show(self, s=""):
    #     print(f"{s:>20} | size: {self.size} | head->", end="")
    #     itr = self.head
    #     while itr:
    #         print(itr.val, end="->")
    #         itr = itr.next
    #     print("null")
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
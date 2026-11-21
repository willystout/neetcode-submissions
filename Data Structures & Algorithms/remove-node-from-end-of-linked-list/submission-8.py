# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        l, r = dummy, head
        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next

        tmp = l
        i = 2
        while tmp and i > 0:
            tmp = tmp.next
            i -= 1
        l.next = tmp


        return dummy.next

        
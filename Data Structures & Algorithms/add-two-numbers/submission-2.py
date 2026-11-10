# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        j = l2
        res = ListNode(0, None)
        dummy = ListNode(0, res)
        car = 0
        while i and j:
            curSum = i.val + j.val + car
            if curSum > 9:
                car = curSum - 10
                res.next = ListNode(car, None)
                car = 1
            else:
                car = 0
                res.next = ListNode(curSum, None)
            res = res.next
            j = j.next
            i = i.next
        while i:
            curSum = i.val + car
            if curSum > 9:
                car = curSum - 10
                res.next = ListNode(car, None)
                car = 1
            else:
                car = 0
                res.next = ListNode(curSum, None)
            res = res.next
            i = i.next
        while j:
            curSum = j.val + car
            if curSum > 9:
                car = curSum - 10
                res.next = ListNode(car, None)
                car = 1
            else:
                car = 0
                res.next = ListNode(curSum, None)
            res = res.next
            j = j.next
        if car > 0:
            res.next = ListNode(car, None)
        return dummy.next.next
            
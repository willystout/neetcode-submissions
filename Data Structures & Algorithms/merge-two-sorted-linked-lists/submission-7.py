# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0, None)
        dummy = ListNode(0, curr)

        while list1 or list2:
            v1 = list1.val if list1 else float("infinity")
            v2 = list2.val if list2 else float("infinity")

            if v1 < v2:
                curr.next = ListNode(v1, None)
                list1 = list1.next
            elif v2 < v1:
                curr.next = ListNode(v2, None)
                list2 = list2.next
            else:
                curr.next = ListNode(v1, None)
                list1 = list1.next
            curr = curr.next
        return dummy.next.next
        
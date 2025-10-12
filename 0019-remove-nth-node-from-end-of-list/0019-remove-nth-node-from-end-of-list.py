# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        curr = head
        if n == count:
            return head.next
        while count - n - 1:
            curr = curr.next
            count -= 1
        curr.next = curr.next.next
        return head

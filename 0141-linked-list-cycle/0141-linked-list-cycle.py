# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head

        while True:
            slow = slow.next
            fast = None if fast.next==None else fast.next.next

            if fast==None:
                return False
            if slow==fast:
                return True

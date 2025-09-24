# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True

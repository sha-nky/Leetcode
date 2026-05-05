# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def lastToFirst(head):
            temp = head
            while temp.next.next:
                temp = temp.next
            
            temp.next.next = head
            head = temp.next
            temp.next = None

            return head
        
        if not head or not head.next:
            return head
        
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        
        k = k % n

        for _ in range(k):
            head = lastToFirst(head)
        
        return head

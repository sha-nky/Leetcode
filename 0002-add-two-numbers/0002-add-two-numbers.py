# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        left, right = l1, l2
        tempHead = ListNode()
        tail = tempHead
        while left and right:
            plus = left.val + right.val + carry
            tail.next = ListNode(plus % 10)
            tail = tail.next
            carry = plus // 10
            left, right = left.next, right.next
        while left:
            plus = left.val + carry
            tail.next = ListNode(plus % 10)
            carry = plus // 10
            tail = tail.next
            left = left.next
        while right:
            plus = right.val + carry
            tail.next = ListNode(plus % 10)
            carry = plus // 10
            tail = tail.next
            right = right.next
        if carry:
            tail.next = ListNode(carry)
        
        return tempHead.next

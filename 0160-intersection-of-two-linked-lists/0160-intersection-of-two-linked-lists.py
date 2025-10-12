# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        hashMap = {}
        pA, pB = headA, headB
        while pA:
            hashMap[pA] = pA.val
            pA = pA.next
        while pB:
            if pB in hashMap:
                return pB
            pB = pB.next
        
        return None

        # if not headA or not headB:
        #     return None
        
        # pA, pB = headA, headB
        # while pA != pB:
        #     pA = pA.next if pA else headB
        #     pB = pB.next if pB else headA
        
        # return pA

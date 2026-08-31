# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance, maxDistance = float("inf"), -float("inf")
        criticalPositions = []

        temp = head.next
        prev = head
        position = 2
        while temp.next:
            if ((temp.val < prev.val and temp.val < temp.next.val) 
                or (temp.val > prev.val and temp.val > temp.next.val)):
                criticalPositions.append(position)
            
            prev = temp
            temp = temp.next
            position += 1
        
        if len(criticalPositions) < 2:
            return [-1, -1]
        
        for i in range(len(criticalPositions)-1):
            minDistance = min(minDistance, criticalPositions[i+1] - criticalPositions[i])
        
        maxDistance = criticalPositions[-1] - criticalPositions[0]

        return [minDistance, maxDistance]

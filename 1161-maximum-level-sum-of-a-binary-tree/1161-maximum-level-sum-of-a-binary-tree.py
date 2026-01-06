# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        maxSum = root.val
        maxLevel = 1

        queue = deque()
        queue.append([1, root])

        while queue:
            total = 0
            size = len(queue)

            for _ in range(size):
                lvl, curr = queue.popleft()
                total += curr.val

                if curr.left:
                    queue.append([lvl+1, curr.left])
                if curr.right:
                    queue.append([lvl+1, curr.right])
            if total > maxSum:
                maxSum = total
                maxLevel = lvl
        
        return maxLevel

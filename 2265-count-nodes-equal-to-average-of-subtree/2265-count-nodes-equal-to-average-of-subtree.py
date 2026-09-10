# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0, 0
            
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            totalSum, totalCount = (leftSum + rightSum + node.val), (leftCount + rightCount + 1)

            if totalSum // totalCount == node.val:
                self.ans += 1
            
            return totalSum, totalCount
        
        dfs(root)
        return self.ans

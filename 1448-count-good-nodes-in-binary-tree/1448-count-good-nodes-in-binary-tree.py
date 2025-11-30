# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0

        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                curMax = node.val
                self.count += 1
            left = dfs(node.left, curMax)
            right = dfs(node.right, curMax)
        
        dfs(root, root.val)
        return self.count

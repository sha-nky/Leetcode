# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return
        
        seen = {}
        
        def dfs(node):
            if not node:
                return False
            if node.val in seen:
                return True
            
            seen[k-node.val] = -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            return left or right
        
        return dfs(root)

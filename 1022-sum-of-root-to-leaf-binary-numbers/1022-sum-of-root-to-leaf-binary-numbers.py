# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node:
                return int(cur, 2)
            
            cur += str(node.val)
            left = dfs(node.left, cur)
            right = dfs(node.right, cur)
            
            return left + right
        
        return dfs(root, "") // 2

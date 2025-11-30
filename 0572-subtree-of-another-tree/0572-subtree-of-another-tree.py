# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def same(x, y):
            if not x and not y:
                return True
            if not x or not y or x.val != y.val:
                return False
            return same(x.left, y.left) and same(x.right, y.right)
        
        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right
        
        return dfs(root)

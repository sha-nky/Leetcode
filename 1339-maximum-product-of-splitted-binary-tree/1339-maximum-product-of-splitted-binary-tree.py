# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.maxProd = -float("inf")
        MOD = 10**9 + 7

        def treeSum(node):
            if not node:
                return 0
            return node.val + treeSum(node.right) + treeSum(node.left)
        
        totalSum = treeSum(root)
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            subtree = node.val + left + right

            self.maxProd = max(self.maxProd, subtree * (totalSum - subtree))
            return subtree
        
        dfs(root)
        return self.maxProd % MOD

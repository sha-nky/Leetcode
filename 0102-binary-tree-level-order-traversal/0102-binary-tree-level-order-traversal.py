# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)

        def rec(node, lvl):
            if not node:
                return []
            result[lvl].append(node.val)
            rec(node.left, lvl+1)
            rec(node.right, lvl+1)
        
        rec(root, 0)
        return list(result.values())

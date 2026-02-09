# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)
        
        def build(left, right):
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            node = TreeNode(arr[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        inOrder(root)
        return build(0, len(arr) - 1)

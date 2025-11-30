# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # queue = deque()
        # queue.append(root)
        # depth = 0
        # while queue:
        #     ls = len(queue)
        #     for _ in range(ls):
        #         curr = queue.popleft()
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
            
        #     depth += 1
        
        # return depth

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left, right) + 1
        
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None: return []
        final = []

        level = [root]
        next_level = []
        while level:
            local = []
            for node in level:
                if node.left is not None: next_level.append(node.left)
                if node.right is not None: next_level.append(node.right)
                local.append(node.val)
            final.append(local)
            level = next_level
            next_level = []

        return final






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.vals = []
        def preorder(node):
            if not node:
                return
            preorder(node.left)
            self.vals.append(node.val)
            preorder(node.right)
        
        preorder(root)
        return self.vals[k-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, min_allowed, max_allowed):
            if root is None: return True
            
            if not (min_allowed < root.val < max_allowed):
                return False
            
            return check(root.left, min_allowed, root.val) and check(root.right, root.val, max_allowed)

        return check(root, float("-inf"), float("inf"))
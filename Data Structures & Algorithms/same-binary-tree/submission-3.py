# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def giveArr(root):
            if root == None: return [None]
            # Pre-Order traversng
            return [root.val] + giveArr(root.left) + giveArr(root.right)
        l1 = giveArr(p)
        l2 = giveArr(q)
        return l1==l2
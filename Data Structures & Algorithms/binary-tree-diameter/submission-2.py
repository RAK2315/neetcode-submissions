# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of a binary tree is the longest path between any two nodes
        ''' logic, at each node, sum the max depth at its left and right,
        and update the global maximum (result) var when ever we get larger sum (left+right)
        then current result'''

        self.ht = 0

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.ht = max(self.ht, left+right)
            return 1 + max(left,right)
        dfs(root)
        return self.ht
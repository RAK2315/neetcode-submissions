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

        # Usung dfs

        self.result = 0 #Here self makes it gloabal

        # returns height/depth
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left+right) # updating global result
            return 1 + max(left,right)
        dfs(root)
        return self.result
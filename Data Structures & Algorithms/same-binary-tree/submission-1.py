# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.li = []
        def trrArr(root):

            if root != None: self.li.append(root.val)
            if root == None:
                self.li.append(None)
                return
            trrArr(root.left)
            trrArr(root.right)
            
        trrArr(p)
        l1 = self.li

        self.li = []
        trrArr(q)
        l2 = self.li

        return l1==l2
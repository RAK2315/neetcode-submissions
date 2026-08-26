# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSameTree(a,b):
            if not a and not b: return True
            if not a or not b: return False
            if a.val == b.val:
                left = isSameTree(a.left, b.left)
                right = isSameTree(a.right, b.right)
                return left and right


        que = [root]

        while que:
            node = que.pop(0)
            if not node: continue 

            if node.val == subRoot.val:
                if isSameTree(node,subRoot):
                    return True
            que.append(node.left)
            que.append(node.right)
        return False
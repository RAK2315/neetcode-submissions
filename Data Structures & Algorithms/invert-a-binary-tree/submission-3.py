# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        # BFS method
        if root is None: return None
        que = [root]
        while que:
            front = que.pop(0)
            front.left, front.right = front.right, front.left
            if front.left:
                que.append(front.left)
            if front.right:
                que.append(front.right)
        return root
        '''

        if root == None:
            return
        root.left, root.right = root.right ,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

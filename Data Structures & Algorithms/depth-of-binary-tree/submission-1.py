# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive dfs
        '''
        if root == None: # if not root
            return 0
        max_depth = max(self.maxDepth(root.left),self.maxDepth(root.right))
        return 1 + max_depth        
        '''
        #BFS
        que = []
        level = 0
        if root: que.append(root)

        # [1  ,2,3  ,null,4, 5,6]
        while que:
            for _ in range(len(que)):
                node = que.pop(0)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            level+=1
        
        return level








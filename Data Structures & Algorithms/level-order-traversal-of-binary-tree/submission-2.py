# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        

        final = []
        que = [root]

        while que:
            length = len(que)
            currLevel = []
            for i in range(length):
                node = que.pop(0)
                if node:
                    currLevel.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if currLevel: final.append(currLevel)   
        
        return final



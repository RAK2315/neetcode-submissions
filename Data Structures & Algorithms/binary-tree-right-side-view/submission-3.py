# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        # BFS

        
        if root is None: return []

        q = deque([root])
        
        result = []

        while q:
            rightmost_node = None
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()
                if node:
                    rightmost_node = node
                    q.append(node.left)
                    q.append(node.right)

            if rightmost_node: result.append(rightmost_node.val)
        return result
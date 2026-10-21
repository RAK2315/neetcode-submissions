class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        """
        Backtracking explained in short
        everything boils donw to these steps
        - recusrion plus tree
        1. base case
        2. decisison to add to the current leaf
        2. decision to NOT add to current leaf
        """

        result = []

        current = []

        def bt_dfs(index):
            if index >= len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            bt_dfs(index + 1)

            current.pop()
            bt_dfs(index + 1)
        bt_dfs(0)
        return result
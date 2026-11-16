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

        def func(index):
            
            if index >= len(nums):
                result.append(current.copy())
                return
            
            current.append(nums[index])
            func(index+1)

            current.pop()
            func(index + 1)
        
        func(0)
        return result
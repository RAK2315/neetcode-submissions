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

        subset = []

        def bt_dfs(index):
            if index >= len(nums): #then we know we are ot of bounds
                # add the current subset to reslt
                result.append(subset.copy())
                return
            
            # decide to add the element
            subset.append(nums[index])
            bt_dfs(index + 1)

            #decide to not add the element
            subset.pop()
            bt_dfs(index + 1)
        
        bt_dfs(0)
        return result
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        # Distict integers given
        # return UNique Combinations

        result = [] #store final res
        current = [] #where we at rn

        def func(index, total): #backtrack+dfs
            if target == total:
                result.append(current.copy())
                return
            
            if index >= len(nums) or total > target:
                return
            
            current.append(nums[index])
            new_total = total + nums[index]
            func(index, new_total)

            current.pop()
            func(index + 1, total)


        func(0,0)
        return result
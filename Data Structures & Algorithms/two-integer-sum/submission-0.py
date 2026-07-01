class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums is [3,4,5,6] target 7 
        store ={}

        for i in range(0,len(nums)): 
            left = target - nums[i]
            if left in store:
                return[store[left],i]
            store[nums[i]]=i
        return []
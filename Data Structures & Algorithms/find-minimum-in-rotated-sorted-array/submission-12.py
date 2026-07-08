class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        res = nums[0]
        while left<=right:
            mid = (left+right)//2
            res = min(res,nums[mid])
            res = min(res,nums[left])

            if nums[mid]>=nums[left]: # Check right
                left = mid+1
            else: #check left
                right = mid - 1
        
        return res


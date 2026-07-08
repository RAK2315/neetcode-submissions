class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target: return mid
            
            # Left sorted potion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid+1
                else: right = mid-1
            # Righ sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: # target> mid value and target < right value
                    left = mid+1

        return -1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        left = 0
        right = k

        maxlist = []

        while right <= len(nums):
            arr = nums[left:right]
            maximum = max(arr)
            maxlist.append(maximum)
            left+=1
            right+=1
        return maxlist

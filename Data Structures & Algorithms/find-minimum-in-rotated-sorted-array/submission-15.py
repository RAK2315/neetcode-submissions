class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        algo:
        the roated sorted array has 2 sorted halfs, left and right
        the min element would be on right sorted half logically 
        [ 3,4,5, 1,2] - min 1

        so if mid ele is greater then right, that means we are currently in left sorted array
            so we update left to move to right side, to potentially come in right sorted array area
        if not that means we are in right sorted aray
            so we can update right to move to left side in right sorted array

        since min is supposed to be on o
            - start from left and right
            while left <= right:
                - mid = left+right //2
                - res = min(res,mid)
                - if mid >= right most
                    left = mid+1
                otherwise:
                    right = mid-1
        """

        left = 0
        right = len(nums)-1

        res = nums[0]

        while left<=right:
            mid = (left+right)//2
            res = min(res, nums[mid])

            if nums[mid] >= nums[right]:
                left = mid+1
            else: right = mid - 1

        return res
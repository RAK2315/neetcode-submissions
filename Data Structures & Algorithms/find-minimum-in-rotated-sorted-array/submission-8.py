class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        Logic
        we check always left and right pointer
        if left< right, that part of arr is sorted
        so minimum becomes ar[left]

        if left>=right, that means that part of arr is not sorted, 
        so min will be in that part

            # logic:
        
            [3,4,5  ,1,2]
            here left = 3, right = 2, mid = 5
            if mid is greater then left, that means its left sorted positon, and we know 
            it wont have the minimum anyway since its rotated ie [3,4,5], and min is in right sorted 
            portion so we update left to increase
            nums[m]>=nums[l]:
                search right

            otherwise if mid is less then left, ie that means now we are in sorted part of array 
            whcih has min ie [1,2]
            else:
                search left

        """
        left = 0
        right = len(nums) - 1

        res = nums[0]
        while left<=right:

            if nums[left]<=nums[right]: # Meaning at 1st iter itself,arr is sorted
                res=min(res,nums[left])
                break
            
            mid = (left+right)//2
            res = min(res,nums[mid])
            if nums[mid]>=nums[left]:
                left=mid+1
            else: right = mid

        return res


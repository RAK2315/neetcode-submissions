class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        final=[]
        for i in range(0,len(nums)):
            product=1
            for j in range(0,len(nums)):
                if i==j:
                    continue
                else:
                    product*=nums[j]
            final.append(product)
        return final

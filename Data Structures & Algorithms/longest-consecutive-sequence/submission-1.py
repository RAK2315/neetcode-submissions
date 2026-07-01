class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        
        We can look at a sorted array FOR UNDERSTANDING
        [100,4,200,1,3,2] -> [1,2,3,4,   100,   200]
        all we hvae to know to see a sequence is if the number previos to and element is in 
        the set
        eg: 1, there is no 0 in array, so its the start of sequence
        eg: 4 - there is 3 in array so its NOT the start of sequence
        eg: 100 - there is no 99 in array so its the start of sequence

        [1,2,3,4] -  size 4
        [100] - size 1
        [200] - size 1
        so longest sequence is 4

        
        """
        """
        This method works but can exceed time complexity and isnt O(n)

        # Lookups in a set is O(1)
        arSet=set(nums)
        final=0
        for i in nums:
            curr=i
            count=0
            while curr in arSet:
                curr+=1
                count+=1
            if count>final:final=count
        return final   
        """

        if not nums:return 0
        numSet=set(nums)
        longest=0

        for n in nums:
            #check if its the start of sequence
            if(n-1) not in numSet:
                length=0
                while n+length in numSet:
                    length+=1
                longest=max(longest,length)
        return longest





















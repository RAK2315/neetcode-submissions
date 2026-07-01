class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        """ 
        original solution i thought of:

        final=[]
        left = 0
        right = len(numbers)-1
        while left<right:
            toFind=target-numbers[left]
            r=right
            while numbers[r]>toFind and r>=left: #till toFind since we know sorted, so nexxt onward elements will be higher 
                r-=1
            if numbers[r]==toFind:
                final.append(left+1)
                final.append(r+1)
                break
            left+=1
        return final
        """

        # after understanding 2 pointers
        left=0
        right=len(numbers)-1

        while left<=right:
            currsum= numbers[left]+numbers[right]
            if currsum>target:
                right-=1
            elif currsum<target:
                left+=1
            else:
                return [left+1,right+1]
            



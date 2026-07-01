class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        final=[]
        left = 0
        right = len(numbers)-1
        while left<right:
            toFind=target-numbers[left]
            r=right
            while numbers[r]>toFind and r>=left:
                r-=1
            if numbers[r]==toFind:
                final.append(left+1)
                final.append(r+1)
                break
            left+=1
        return final

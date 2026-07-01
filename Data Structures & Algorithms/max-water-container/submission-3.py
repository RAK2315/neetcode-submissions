class Solution:
    def maxArea(self, hts: List[int]) -> int:

        left=0
        right=len(hts)-1

        area=0

        while left<right:
            ar = min(hts[left],hts[right])*(right-left)
            if hts[left]>=hts[right]:
                right-=1
            else:
                left+=1
            area=max(area,ar)

        return area
class Solution:
    def trap(self, hts: List[int]) -> int:

        if not hts: return 0


        left=0
        right=len(hts)-1
        maxleft=hts[left]
        maxright=hts[right]

        area=0
        while left<right:

            if maxleft<=maxright:
                left+=1
                maxleft=max(maxleft,hts[left])
                area+=maxleft-hts[left] #will be 0 or positve always

            else: 
                right-=1
                maxright=max(maxright,hts[right])
                area+=maxright-hts[right]

        return area

        """
        the logic, we calculate the amt of water stored at each index
            - first and last elemnts cant store any water, logically
            - then onwards elemtns cant store water only if they are less then left and right
            - so keep track of left max and right max:
                - if leftmax less the right max:
                    - we increase left
                    - check to set new leftmax
                    - add the calculated area [ min(maxleft,maxright)-current_height]
                - if leftmax is more:
                    - we decrease right
                    - check t set new maxrigh
                    - add to calculated area
        """

        
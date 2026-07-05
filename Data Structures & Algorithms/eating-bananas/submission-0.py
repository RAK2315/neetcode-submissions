class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        left = 1
        right = max(piles)

        speeds=[]

        while left<=right:

            mid = (left+right)//2 #speed
            totaltime=0
            for pile in piles:
                totaltime+=math.ceil(float(pile)/mid) # pile/speed
            if totaltime<=h:
                speeds.append(mid)
                right = mid-1
            else:
                left = mid+1
        return min(speeds)
        
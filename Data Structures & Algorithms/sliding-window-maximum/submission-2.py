class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using a deque since we observer first ele that enters is removed in same sequnce

        # store indices in deque
        deq = []

        output = []

        left = right = 0    

        while right < len(nums):

            # remove indices of ele's smaller then current right
            while deq and nums[ deq[-1] ] < nums[right]:
                deq.pop()
            
            # add the curent right element index ie current max
            deq.append(right)

            # if left pointer passes front index, remvoe it
            # since outside window
            if left > deq[0]:
                deq.pop(0)
            
            # once window reaches sizez k, the forn of deque is the max , add to output
            if (right+1) >= k:
                output.append(nums[ deq[0] ])
                left += 1
            
            right += 1
        return output
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        """ 
        MY SOLUTION before stack
        
        final=[]
        for i in range(len(temps)):
            j=i
            count=0
            foundLarger=False
            while j<len(temps):
                if temps[j]>temps[i]:
                    foundLarger=True
                    break
                j+=1
                count+=1
            
            if foundLarger: final.append(count)
            else: final.append(0)
        return final

        worst case: o(n2)
        """

        final=[0]*len(temps)
        stack=[]
        for index, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]: # While current temp is greater than the last stacked temp
                stackIndex = stack.pop()
                final[stackIndex] = index - stackIndex   # Distance to warmer day
            stack.append(index)  #Push current temp and index onto stack
        return final



















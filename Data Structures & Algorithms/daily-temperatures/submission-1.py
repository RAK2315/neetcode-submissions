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
        stack=[] # [temp,index]
        for index,temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                stackTemp,stackIndex = stack.pop()
                final[stackIndex]=index-stackIndex
            stack.append([temp,index])
        return final



















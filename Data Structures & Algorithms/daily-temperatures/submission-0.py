class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        

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
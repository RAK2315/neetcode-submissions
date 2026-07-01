class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        results={}
        final=[]
        for i in nums:
            if i not in results:
                results[i]=1
            else:
                results[i]+=1

        for key,value in results.items():
            if(len(final)<k):
                final.append(key)
            else:
                # ex final=[2,3]
                # assigning intial minkey as final[0]
                minkey=final[0]

                # Finding the ele in final with min no.of appearences in nums list
                for num in final:
                    if results[num]<results[minkey]:
                        minkey=num
                    
                # Checking if new key has more appearences
                # If so, remove current lowest and add the new one
                if value > results[minkey]:
                    final.remove(minkey)
                    final.append(key)
                
        return final
                        


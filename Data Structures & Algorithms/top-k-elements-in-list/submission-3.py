class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Questions ask to find top k frquent elements
        ie k elements with most appearences
        eg- [1,1,2,2,2,3,3,4,4,4], k=2
        most number of appearneces: 2 has 3 appearences, and 4 has 3 appearences
        question also says that cases wouldnt have repetition tied like [3,3,4,4], k=1
        so it would either be [3,3],k=1 or [3,3,4,4,4],k=1
        """
        results={}
        final=[]
        for i in nums:
            if i not in results:
                results[i]=1
            else:
                results[i]+=1

        for key,value in results.items():
            # Filling the final list till it reaches k elements
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
                        


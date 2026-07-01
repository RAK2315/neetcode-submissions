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
            if (len(final)<k):
                final.append(key)
            
            else:
                min_val_key = final[0]
                for num in final:
                    if results[num] < results[min_val_key]:
                        min_val_key = num
                
                if value > results[min_val_key]:
                    final.remove(min_val_key)
                    final.append(key)

        return final

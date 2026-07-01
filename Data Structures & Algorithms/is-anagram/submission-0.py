class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        def counter(d1: dict,string: str):
            for char in string:
                if char in d1.keys():
                    count = d1[char]
                    count+=1
                    d1[char]=count
                else:
                    d1[char]=1   
        d1={}
        d2={}
        counter(d1,s)
        counter(d2,t)
        return d1==d2   

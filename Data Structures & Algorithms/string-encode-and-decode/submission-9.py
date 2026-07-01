class Solution:

    def encode(self, strs: List[str]) -> str:

        # stucture - size#word
        res=""
        for word in strs:
            res+=str(len(word))
            res+="#"
            res+=word
        return res

    def decode(self, s: str) -> List[str]:
        

        count=0
        final=[]
        # 5#hello5#world
        while count<len(s):
            j=count
            while s[j]!="#":
                j+=1
            size = int(s[count:j])
            word = s[j+1:j+size+1]
            count=j+size+1
            final.append(word)
        return final

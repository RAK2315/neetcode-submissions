class Solution:

    def encode(self, strs: List[str]) -> str:
        # ord(char) takes a char and converts to ascii
        # chr(int) takes a number ie ascii converts to char

        """
        if strs==[]:
            return "0#"
        shift=10
        encoded=""
        for word in strs:
            temp=""
            for char in word:
                newchar=chr(ord(char)+shift)
                temp+=newchar
            encoded+=temp
            encoded+="#"
        return encoded[:-1]
        """

        # Method 2
        res=[]
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        if s=="0#":
            return []
        shift=10
        temp=list(s.split("#"))
        final=[]
        for word in temp:
            temp=""
            for char in word:
                newchar=chr(ord(char)-shift)
                temp+=newchar
            final.append(temp)
        return final
        """

        final=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            i=j+1
            j=j+1+length
            word=s[i:j]
            final.append(word)
            i=j
        return final




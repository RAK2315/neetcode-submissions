class Solution:

    def encode(self, strs: List[str]) -> str:
        # ord(char) takes a char and converts to ascii
        # chr(int) takes a number ie ascii converts to char

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


    def decode(self, s: str) -> List[str]:
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


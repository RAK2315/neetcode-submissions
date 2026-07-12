class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        original = {}
        for i in s1:
            if i not in original:
                original[i] = 1
            else: original[i]+=1
        

        window = len(s1)
        pointer = 0
        for i in range(len(s2)):
            w = s2[pointer:window+pointer]
            local = {}
            for i in w:
                if i not in local: local[i] = 1
                else: local[i] += 1
            if local == original: return True
            pointer+=1
        return False
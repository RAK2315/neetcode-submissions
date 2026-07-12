class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False



        original = {}
        for i in s1:
            if i not in original:
                original[i] = 0
            original[i]+=1

        window = {}
        for i in range(len(s1)):
            if s2[i] not in window:
                window[ s2[i] ] = 0
            window[ s2[i] ] +=1
        
        if window == original : return True
        
        left = 0
        for right in range(len(s1),len(s2)):
            
            l_char = s2[left]
            window[l_char] -= 1
            if window[l_char] == 0: del window[l_char]
            left += 1

            new_char = s2[right]
            if new_char not in window:
                window[new_char] = 0
            window[new_char] += 1

            if window == original: return True

        return False
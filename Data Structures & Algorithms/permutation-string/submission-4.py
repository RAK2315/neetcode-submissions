class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # edge case
        if len(s1) > len(s2): return False

        # creat hash for original s1
        original = {}
        for char in s1:
            if char not in original:
                original[char] = 0
            original[char] += 1

        # create hash for 1st window
        w = len(s1)
        window = {}
        for i in range(w):
            if s2[i] not in window:
                window[ s2[i] ] = 0
            window[ s2[i] ] += 1

        if window == original: return True


        # form there onwards, move thoriugh the str, adding and removing elements, comparing 
        # this with original hash map

        left = 0
        for right in range(len(s1), len(s2)):
            left_char = s2[left]
            window[left_char] -= 1
            if window[left_char] == 0: del window[left_char]
            left += 1

            right_char = s2[right]
            if right_char not in window:
                window[right_char] = 0
            window[right_char] += 1

            if window == original: return True
        
        return False
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # the idea is that this quesiton doesnt really need actualy replacements

        left = right = 0
        replacementLimit = k

        longest = 0

        count = {}
        while right < len(s):
            if s[right] not in count: count[ s[right] ] = 1
            else: count[ s[right] ] += 1

            maxletter = max(count.values())

            windowLen = (right-left) + 1
            
            if (windowLen - maxletter) <= replacementLimit:
                longest = max(longest, windowLen)
            else:
                count[ s[left] ]-=1
                left+=1
            right+=1


        return longest
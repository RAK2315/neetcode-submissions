class Solution:
    def minWindow(self, s: str, target: str) -> str:

        # Edge case
        if len(target) > len(s): return ""
        if target=="": return ""
        if s=="": return ""

        # eg A D O B E C O D E B A N C
        # target A B C

        freq_map ={}
        for i in target:
            if i not in freq_map: freq_map[i] = 0
            freq_map[i] += 1

        window = {}

        have = 0
        need = len(freq_map)

        result = [-1, -1]
        resLen = float("infinity") # cause everythgn is less then infinity

        left = 0

        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 0
            window[s[right]] += 1

            if s[right] in freq_map and freq_map[s[right]]==window[s[right]]:
                have += 1
            
            while have == need:
                res = [left,right]
                l = right-left+ 1
                if l< resLen:
                    resLen = l
                    result = res

                window[ s[left] ] -= 1
                if s[left] in freq_map and window[s[left]] < freq_map[s[left]]:
                    have -= 1

                left += 1
        

        if resLen != float('infinity'): return s[ result[0] : result[1]+1]
        else: return ""





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        - for every char in string:
        - initialise: left, right, longest, seen = set()
        - left pointer at char, 
        - we increment right pointer
            - if right is not in seen:
                - add it to set
                - increment right
                - longest len would be right (index - lefts) + 1
                - check it with current with longest
            
            other wise right is in set:
                - remove it from set aka the left
                (since right adds to seen, when a char appears thats already in seen
                that means its the saem as the current left)
                - increment left
        
        - return longest
        """

        left = right = 0

        longest = 0

        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add( s[right] )
                length = (right-left)+1
                longest = max(longest, length)
                right += 1
            
            else:
                seen.remove( s[left] )
                left += 1
        
        return longest
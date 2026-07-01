class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res=""
        for i in s.lower():
            if i.isalnum():
                res+=i
        return res==res[::-1]         
class Solution:
    def isValid(self, s: str) -> bool:
        
        bracks={")":"(", "}":"{","]":"["}
        stack=[]

        for bracket in s:
            if bracket not in bracks:
                stack.append(bracket)
            else:
                if not stack or stack.pop()!=bracks[bracket]:
                    return False
        if not stack: return True
        else: return False

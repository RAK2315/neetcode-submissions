class Solution:
    def isValid(self, s: str) -> bool:
        
        bracks={")":"(", "}":"{","]":"["}
        stack=[]

        for bracket in s:
            if bracket not in bracks:
                stack.append(bracket)
                # if current is not closing bracket, ie open bracket so push to stack

            else:
                if not stack or stack.pop()!=bracks[bracket]:
                # otherwise check if stack empty or
                # last/top ele of stack is NOT corresponding to current closing elemtn
                # then invalid
                    return False

        # if stack is not empty then invalid, this condition is for ex: s="["
        # this would only push to stack never pop 
        if not stack: return True
        else: return False

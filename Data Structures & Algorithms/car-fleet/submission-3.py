class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if len(position)==1: return 1
        cars =[] # [postion, speed]
        for i in range(len(position)):
            cars.append([position[i],speed[i]])

        cars.sort()

        stack=[]


        # Trial ; [[3,2],[1,4]]

        for pos,speed in cars[::-1]:
            time_taken = (target-pos)/speed
            stack.append(time_taken)
            # If len stack is 2 or more then only it cheks the 2nd condition
            if len(stack)>1 and time_taken <= stack[-2] :
                stack.pop()
        return len(stack)


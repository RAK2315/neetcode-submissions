class MinStack:

    def __init__(self):
        self.stack=[]     
        self.minstack=[]   


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:  # if minstack empty, 
            self.minstack.append(self.stack[-1]) #ie "minimum"  defaults to first number added to stack
        else:
            # otherwise we know minstack's top is minimum elemnt
            # we compare with new added val to see if a new min has appeared
            minimum=min(self.minstack[-1],val) 
            self.minstack.append(minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]

        
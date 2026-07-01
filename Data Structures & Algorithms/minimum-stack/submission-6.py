class MinStack:

    def __init__(self):
        self.stack=[]     
        self.minstack=[]   
        self.minimum=0


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minimum=self.stack[-1]
            self.minstack.append(self.minimum)
        else:
            self.minimum=min(self.minimum,val)
            self.minstack.append(self.minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.minstack: self.minimum=self.minstack[-1]
        else: self.minimum=0
    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]

        # [-2,0,2,]
        # [-2,-2,-2,]
        

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minval = 10**1000
        

    def push(self, val: int) -> None:
        self.stack.append(val)


        if not self.minstack or val < self.minstack[-1]: 
            self.minstack.append(val) 
        else: 
            self.minstack.append(self.minstack[-1])

        print(self.minstack)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.minstack: 
            self.minval = self.minstack[-1] 

        ##print(self.minstack)

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        

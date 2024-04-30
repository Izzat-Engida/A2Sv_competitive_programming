
class MinStack:

    def __init__(self):
        self.head=[]
        self.tail=[]
        

    def push(self, val: int) -> None:
        self.head.append(val)
        if self.tail:
            val=min(val,self.tail[-1])
        self.tail.append(val)

    def pop(self) -> None:
        self.head.pop()
        self.tail.pop()

    def top(self) -> int:
        return self.head[-1]  

    def getMin(self) -> int:
        return self.tail[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class MyCircularQueue:

    def __init__(self, k: int):
        self.head=self.tail=None
        self.size=0
        self.capacity=k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp=node(value)
        if self.isEmpty():
            self.head=self.tail=temp
            self.tail.next=self.head
        else:
            self.tail.next=temp
            self.tail=temp
            self.tail.next=self.head  
        self.size+=1    
        return True  

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head=self.head.next
        self.tail.next=self.head
        self.size-=1
        if self.isEmpty():
            self.tail=None
        return True    

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.data   
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.data   
        

    def isEmpty(self) -> bool:
        return self.size==0        

    def isFull(self) -> bool:
        return self.size==self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

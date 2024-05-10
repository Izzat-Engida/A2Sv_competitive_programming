class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def get(self, index: int) -> int:
        temp=self.head
        count=0
        while temp is not None:
            if index==count:
                return temp.value
            count+=1
            temp=temp.next  
        return -1      

    def addAtHead(self, val: int) -> None:
        newnode=node(val)
        if self.head is None:
            self.head=newnode
            self.tail=self.head
        else:
            newnode.next=self.head
            self.head=newnode    

    def addAtTail(self, val: int) -> None:
        newnode=node(val)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or(self.head is None and index>0):
            return
        elif index==0:
            self.addAtHead(val)
        else:
            newnode=node(val)
            temp=self.head
            for _ in range(index-1):
                if temp is None:
                    return
                temp=temp.next
            if temp:    
                newnode.next=temp.next
                temp.next=newnode
                if newnode.next is None:
                    self.tail=newnode                

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head is None:
            return
        elif index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            temp = self.head
            prev=None
            count=0
            while temp and count<index:
                prev=temp
                temp=temp.next
                count+=1
            if temp:
                prev.next=temp.next
                if temp.next is None:
                    self.tail=prev     
         

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class RecentCounter:

    def __init__(self):
        self.temp=[]

    def ping(self, t: int) -> int:
        self.temp.append(t)
        while (t-self.temp[0])>3000:
            self.temp.pop(0) 
        return len(self.temp)    
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

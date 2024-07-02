class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in range(len(stones)):
            temp=-stones[i]
            heapq.heappush(heap,temp)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x!=y:
                temp=abs(x-y)
                heapq.heappush(heap,-temp)
        return -heap[0] if len(heap)==1 else 0       
        

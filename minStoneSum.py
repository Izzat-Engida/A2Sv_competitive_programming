class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for i in range(len(piles)):
            n=-1 * piles[i]
            heapq.heappush(heap,(n))
        while k:
            temp=-1 * (heapq.heappop(heap))
            te = math.floor(-temp / 2)
            heapq.heappush(heap,te)
            k-=1
        su=0    
        while heap:
            temp=-1 * (heapq.heappop(heap))
            su+=temp
        return su    

        

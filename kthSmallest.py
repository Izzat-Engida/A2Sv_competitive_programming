class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        size=len(matrix)
    
        for i in range(size):
            for j in range(size):
                t=-matrix[i][j]
                if len(heap)<k:
                    heapq.heappush(heap,-matrix[i][j])
                elif t>heap[0]:
                    heapq.heappushpop(heap,t)
        return -heap[0]              
                 

        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for w in words:
            d.setdefault(w, 0)  
            d[w] += 1
        heap = []
        for t in d:
            heapq.heappush(heap, (-d[t], t))
        ans = []
        for _ in range(k):
            key, word = heapq.heappop(heap)
            ans.append(word)
        return ans

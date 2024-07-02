class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        size = len(tasks)
        tasks = [(tasks[i], i) for i in range(size)]
        tasks.sort()
        minheap = []
        answer = []
        time = 0
        for (e, p), i in tasks:
            while minheap and time < e:
                pr, ind = heapq.heappop(minheap)
                answer.append(ind)
                time += pr
            if not minheap:
                time = max(time, e)
            heapq.heappush(minheap, (p, i))
        while minheap:
            ct, ci = heapq.heappop(minheap)
            answer.append(ci)
        return answer

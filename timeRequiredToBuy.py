class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([(i, ticket) for i, ticket in enumerate(tickets)])
        count = 0
        while True:
            i, t = q.popleft()
            count += 1
            if i == k and t == 1:
                return count
            if t > 1:
                q.append((i, t - 1))  
        return count

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(ticket, i) for i, ticket in enumerate(tickets)])
        time = 0
        while True:
            ticket, i = queue.popleft()
            time += 1
            if i == k and ticket == 1:
                return time
            if ticket > 1:
                queue.append((ticket - 1, i))

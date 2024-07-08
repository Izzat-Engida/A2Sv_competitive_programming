class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        q = deque()
        q.append("0000")
        visited.add("0000")
        moves = 0

        if "0000" in deadends:
            return -1

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == target:
                    return moves
                for i in range(4):
                    for d in [-1, 1]:
                        next_digit = (int(curr[i]) + d) % 10
                        next_state = curr[:i] + str(next_digit) + curr[i + 1:]
                        if next_state not in deadends and next_state not in visited:
                            visited.add(next_state)
                            q.append(next_state)
            moves += 1

        return -1


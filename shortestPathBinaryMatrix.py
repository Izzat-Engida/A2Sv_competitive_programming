from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        destination = [size - 1, size - 1]
        def check(i, j):
            return 0 <= i < size and 0 <= j < size
        q = deque()
        count=0
        visit = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        if grid[0][0] == 0:
            q.append((0, 0, 1))  
            visit.add((0, 0))
        while q:
            temp1, temp2, count = q.popleft()
            if [temp1, temp2] == destination:
                return count
            for a, b in directions:
                u, t = temp1 + a, temp2 + b
                if check(u, t) and grid[u][t] == 0 and (u, t) not in visit:
                    q.append((u, t, count + 1))
                    visit.add((u, t))

        return -1

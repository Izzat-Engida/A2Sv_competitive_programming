class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        
        def check(i, j):
            return 0 <= i < row and 0 <= j < col

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(entrance[0], entrance[1], 0)]) 
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while q:
            temp1, temp2, count = q.popleft()
            for a, b in directions:
                t, u = temp1 + a, temp2 + b
                if check(t, u) and maze[t][u] == '.' and (t, u) not in visited:
                    if (t == 0 or t == row - 1 or u == 0 or u == col - 1) and [t, u] != entrance:
                        return count + 1
                    q.append((t, u, count + 1))
                    visited.add((t, u))

        return -1

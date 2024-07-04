class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set()
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
            for n in rooms[node]:
                if n not in visited:    
                    q.append(n)
        return len(visited) == len(rooms)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit=set()
        def dfs(node, parent): 
            temp=0 
            for nei in graph[node]:
                if nei!=parent:
                    time=dfs(nei,node)
                    if time>0 or hasApple[nei]:
                        temp+=time+2
            return temp
        return dfs(0,-1)                


     

        

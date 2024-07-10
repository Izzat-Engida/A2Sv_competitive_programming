class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
       
        
        def dfs(node,visited,path,target):
            if node==target:
                result.append(path)
                return
            visited.add(node)
            for a in graph[node]:
                if a not in visited:
                    dfs(a,visited,path+[a],target)
            visited.remove(node)
        result=[]
        dfs(0,set(),[0],len(graph)-1) 
        return result           

                


        

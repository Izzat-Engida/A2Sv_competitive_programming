"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        arr={e.id:e for e in employees}
   
        def dfs(id):
            temp=arr[id]
            tot=temp.importance
            for c in temp.subordinates:
                tot+=dfs(c)
            return tot
        return dfs(id)            

        

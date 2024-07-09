"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
                return 0
        def dfs(root):
            count=0 
            if not root.children:
                return 1   
            for c in root.children:
                count=max(dfs(c),count)
            return count+1
        return dfs(root)            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer=0
        def dfs(root,max_val,min_val):
            if not root:
                return 
            self.answer=max(self.answer,abs(root.val-max_val),abs(root.val-min_val)) 
            max_val=max(max_val,root.val)
            min_val=min(min_val,root.val)
            dfs(root.left,max_val,min_val)
            dfs(root.right,max_val,min_val)
        dfs(root,root.val,root.val)
        return self.answer    





        

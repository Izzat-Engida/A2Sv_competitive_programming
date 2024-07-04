# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        array=[root.val]  
        q=deque([root])  
        while q:
            
            su=0
            count=0
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    su+=node.left.val
                    count+=1
                if node.right:
                    q.append(node.right)
                    su+=node.right.val
                    count+=1
            if count>=1:
                array.append(su/count)
            
        return array       
 
        

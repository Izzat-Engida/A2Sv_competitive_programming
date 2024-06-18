# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        order=[]
        queue=deque([root])
        switch=True
    
        while queue:
            size=len(queue)
            temp=[]
            for i in range(size):
                node=queue.popleft()
                if switch:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)    
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            order.append(temp)
            switch=not switch
        return order                
        

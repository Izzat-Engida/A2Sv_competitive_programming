# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        order=[]
        queue=[]
        queue.append(root)
        while queue:
            size=len(queue)
            temp=[]
            for i in range(size):
                node=queue[0]
                queue=queue[1:]
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            order.append(temp)
        return order                

      

        

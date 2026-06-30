# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        temp = []
        result = []
        if not root: 
            return []

        while q: 
            level_size = len(q)
            

            
            for i in range(0, level_size): 

                va = q.popleft()
                if va: 
                    temp.append(va.val)

                    if va.left: 
                        q.append(va.left)
                    if va.right: 
                        q.append(va.right)
            
            result.append(temp)
            temp = []
        
        return result   


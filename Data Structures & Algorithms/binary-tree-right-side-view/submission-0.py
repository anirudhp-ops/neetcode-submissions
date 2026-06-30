# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque() 
        q.append(root)
        result = []
        
        if not root: 
            return []
        
        while q: 
            level_len = len(q) 
            node = q[-1]
            result.append(node.val)
            for i in range(0, level_len): 
                curr = q.popleft() 
                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)
            
        return result
            

        
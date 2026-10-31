# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [] 
        
        def dfs(root, k): 
            if not root: 
                return 
            else: 
                dfs(root.left, k) 
                count.append(root.val)
                dfs(root.right, k)
                
        dfs(root, k)

        return count[k-1]


        
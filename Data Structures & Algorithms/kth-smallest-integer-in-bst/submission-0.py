# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, count, k): 
            if not root: 
                return count
            else: 
                
                dfs(root.left, count, k) 
                count.append(root.val)
                dfs(root.right, count, k)
                
            return count

            
            
            

        return dfs(root, [], k)[k-1]


        
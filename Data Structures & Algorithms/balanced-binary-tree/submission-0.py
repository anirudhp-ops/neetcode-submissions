# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): 

            if not node: 
                return [True, 0]
            
            right = dfs(node.right)
            left = dfs(node.left) 

            

            balance = abs(left[1] - right[1]) <= 1 
            height = max(left[1], right[1]) + 1 

            if not left[0] or not right[0]: 
                balance = False
            
            return [balance, height]
        
        return dfs(root)[0]





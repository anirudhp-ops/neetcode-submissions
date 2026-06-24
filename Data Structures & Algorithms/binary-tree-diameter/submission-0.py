# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node): 

            if not node: 
                return [0, 0]
           
            else: 

                right = dfs(node.right)
                left = dfs(node.left)

                height = 1 + max(right[0], left[0]) 

                checker = right[0] + left[0] 

                return [height, max(checker, max(right[1], left[1]))]
        
        
        return dfs(root)[1]






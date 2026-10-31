# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        
        def dfs(root, val): 

            if not root: 
                return 

            if not root.left and val < root.val: 
                root.left = TreeNode(val)
            elif not root.right and val > root.val: 
                root.right = TreeNode(val)

            
            if val < root.val: 
                dfs(root.left, val)
            
            elif val > root.val: 
                dfs(root.right, val)
        
        if not root: 
            return TreeNode(val)
        
        dfs(root, val)
        return root

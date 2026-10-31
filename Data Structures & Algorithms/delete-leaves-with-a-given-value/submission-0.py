# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# post order recursion
# continuesly iteate to leaf node 
# check - if leaf node and if target delete 

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root, target): 
            if not root: 
                return None
            
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)

            if root.val != target: 
                return root 
            
            elif not root.left and not root.right and root.val == target:
                return None 
            
            return root 


        

        return dfs(root, target) 
        
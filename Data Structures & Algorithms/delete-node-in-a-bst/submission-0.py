# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Traverse throught the array to find node - log n time
# replace the current node with node.left.right or node.right.left
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root: 
            return 
        
        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        
        else: 
            if not root.right and not root.left: 
                return 
            
            if not root.right: 
                return root.left
            
            elif not root.left: 
                return root.right 

            
            else: 
                storage = root.right 
                
                while storage.left: 
                    storage = storage.left 
                
                root.val = storage.val 

                root.right = self.deleteNode(root.right, storage.val)
            
        return root 

            



            


        
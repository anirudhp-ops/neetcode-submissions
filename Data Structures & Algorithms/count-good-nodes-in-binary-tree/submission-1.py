# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val): 
            if not root: 
                return 0 
            val = max_val
            good = 0

            if root.val > max_val:
                max_val = root.val

            if root.right and root.right.val >= root.val and root.right.val >= max_val: 
                good += 1 
                
            if root.left and root.left.val >= root.val and root.left.val >= max_val: 
                good += 1 
                

            print(good)
            

            return good + dfs(root.right, max_val) + dfs(root.left, max_val) 
       
        # +1 for the root node 
        
        return dfs(root, root.val) + 1

        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True 
        elif not root: 
            return False
        elif root.val != subRoot.val: 
            print("eehho")
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else: 
            print(root.val) 
            print(subRoot.val)
            print("boom")
            def isSameTree(node, subnode):
                print("inside")
                
                if not subnode and not node: 
                    return True 
                elif not subnode: 
                    return False
                elif not node: 
                    return False
                
                elif node.val != subnode.val: 
                    return False

                else: 
                    
                    return isSameTree(node.right, subnode.right) and isSameTree(node.left, subnode.left)
            if isSameTree(root, subRoot): 
                return True 
            else: 
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


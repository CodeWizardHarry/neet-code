# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """"
        Given the root of a binary tree, invert the tree
        
        Returns:
        - TreeeNode: Root of the tree
        
        """
        
        if not root:
            return None
        
        temp = root.left   
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
        
        
      
    
        #official solution
        # if not root:
        #     return None

        # # swap the children
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

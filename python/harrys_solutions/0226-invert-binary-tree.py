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
        
        def dfs(root):
            if not root:
                return 

            temp = root.left
            root.left = root.right
            root.right = temp
            
            dfs(root.left)
            dfs(root.right)

            return root 

        return dfs(root)


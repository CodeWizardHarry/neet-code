# Definition for a binary tree node.

""""
Notes:
1. need to create two important variable
2. one to track the res , which is the max length of the overall tree
3. one to track current node's max depth

"""



from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        """
        steps:
        1. create a recursive function that finds the maxdepth at each node(same as maxDpeth
           function just need a bit modification)
        2. create a res variable that tracks the max diameter
           res = max(res, left + right)
           
        3. return res
        """
        res = 0  # tracks the length of the longest path

        # returns the height of each node and tracks res
        # it's just a modified version of the maxDepth function
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)  
            right = dfs(root.right)  
            # notice that the only difference between this question and
            # 104 - maximum Depth of Binary Tree is the extra line added below
            res = max(res, left + right)    

            return 1 + max(left, right)  

        dfs(root)
        return res

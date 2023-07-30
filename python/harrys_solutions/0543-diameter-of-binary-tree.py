# Definition for a binary tree node.
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

            left = dfs(root.left)  # height of left node
            right = dfs(root.right)  # height of right node
            res = max(res, left + right)  # tracks the max diameter of the entire tree

            return 1 + max(left, right)  # tracks the height of the current root - same as the maxDpeth function

        dfs(root)
        return res

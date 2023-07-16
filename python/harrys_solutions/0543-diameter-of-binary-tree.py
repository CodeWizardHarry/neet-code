# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # tracks the length of the longest path

        # returns the height of each node and tracks res
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)  # height of left node
            right = dfs(root.right)  # height of right node
            res = max(res, left + right)  # tracks the diameter of the entire tree

            return 1 + max(left, right)  # tracks the height of the current root

        dfs(root)
        return res

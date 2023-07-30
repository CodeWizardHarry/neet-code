# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.

        Steps:
        1. start from the bottom of the tree and apply dfs
           to check if each subtree is height-balanced
        2. determine if abs(left.height - right.height) <= 1
        2. create an array for each dsf to track [balance_status, height of current tree]
        3.

        Returns:
            True if it's height-balanced tree, otherwise return false
        """

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            height = 1 + max(
                left, right
            )  # tracks height of the current node, height of a tree is the number of layers in a tree

            return [balanced, height]

        return dfs(root)[0]

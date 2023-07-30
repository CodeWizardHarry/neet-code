# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # both tree are empty
        if not p and not q:
            return True
        # one of the trees is empty or if the two nodes have the same val
        if not p or not q or p.val != q.val:
            return False
        
        is_same = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return is_same


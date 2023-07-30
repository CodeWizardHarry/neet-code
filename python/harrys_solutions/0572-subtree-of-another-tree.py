# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        is_sub = self.isSameTree(s.left, t.left) or self.isSameTree(s.right, t.right)

        
        
        
        
        
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # both tree are empty
        if not p and not q:
            return True
        # one of the trees is empty or if the two nodes have the same val
        if not p or not q or p.val != q.val:
            return False

        is_same = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return is_same

        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False

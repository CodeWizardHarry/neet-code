from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # Recursive
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        
        helper(root)
        return res

def run_tests():
    # Test case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print("Test case 1 output:", Solution().inorderTraversal(root1)) # Expected: [1, 3, 2]

    # Test case 2
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(7)
    print("Test case 2 output:", Solution().inorderTraversal(root2)) # Expected: [1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    run_tests()

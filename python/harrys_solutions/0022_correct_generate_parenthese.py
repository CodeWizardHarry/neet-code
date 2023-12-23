#GPT

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []

        def dfs(total):
            # Check if the current state is invalid or if we've reached the solution
            if total < 0 or len(subset) > 2 * n:
                return
            if len(subset) == 2 * n and total == 0:
                res.append(''.join(subset))
                return

            # Add an open parenthesis
            subset.append('(')
            dfs(total + 1)
            subset.pop()

            # Add a close parenthesis
            subset.append(')')
            dfs(total - 1)
            subset.pop()

        dfs(0)
        return res

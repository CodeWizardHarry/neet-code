# this solution is wrong can you tell why its wrong?



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset= []
        res = []
        total = 0
        
        def dfs(total):
            if len(subset) > 2*n or total < 0 :
                return
            if len(subset) == 2*n and total == 0:
                res.append(''.join(subset))
                return

            subset.append('(')
            # mistake 1, this is not the same as dfs(total + 1)
            # when you backtrack you need to undo the changes you made
            # but if you use dfs(total + 1), you don't need to undo anything, 
            # because total stays unchanged. 
            total += 1
            dfs(total)  
            subset.pop()
            
            subset.append(')')
            total -= 1
            dfs(total)
            # mistake 2, you need to add pop() here

        dfs(0)
        return res

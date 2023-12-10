# this version is esier to understand, from leetcode solutions by lukskywalkerrr
# nums[:] is a shallow copy, sufficient because integers are immutable

class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, used):
            if len(path) == len(l):
                res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
                return

            for i, letter in enumerate(l):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                path.append(letter)
                used[i] = True
                dfs(path, used)
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False
            
        dfs([], [False] * len(l))
        return res
    
    
    
## gpt4 solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # If all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # Place i-th integer first in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # Use next integers to complete the permutations
                backtrack(first + 1)
                # Backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

# Example usage:

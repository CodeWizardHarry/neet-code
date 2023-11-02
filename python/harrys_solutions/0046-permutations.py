# this version is esier to understand, from leetcode solutions by lukskywalkerrr
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
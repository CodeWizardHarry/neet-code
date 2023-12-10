class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        res=[]

        def dfs(i,total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1,total+candidates[i])

            subset.pop()

            ## print(len(candidates)) = 7
            ## print(i) =6 i+1=7 -> out of obound
            # while candidates[i]==candidates[i+1] and  i+1 < len(candidates): -- this gives index out of rnage error
            while  i+1 < len(candidates) and candidates[i]==candidates[i+1] :
                i += 1
            dfs(i+1,total)

        dfs(0, total=0)
        return res
        
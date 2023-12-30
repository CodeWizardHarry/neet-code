class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dvvf
        l = r = 0
        subset = set()
        res = 0
        while r<len(s):
            if s[r] not in subset:
                subset.add(s[r])
                res = max(len(subset),res)
            else:
                while s[r] in subset:
                    subset.remove(s[l])
                    l += 1
                subset.add(s[r])
                print(subset)
                
            r += 1
        print(subset)
        return res 
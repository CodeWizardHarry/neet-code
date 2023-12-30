class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        res = 0
        count_dict = dict()

        for i in range(len(s)):
            r = i
            count_dict[s[i]] = count_dict.get(s[i], 0) + 1

            temp_sum = r-l+1
            temp_max = max([val for key, val in count_dict.items()])

            # decrease k till it's happy
            while temp_sum - temp_max > k :
                count_dict[s[l]] -= 1
                l += 1

                temp_sum = r-l+1
                temp_max = max([val for key, val in count_dict.items()])
            res = max(res, r-l +1)
        return res
        
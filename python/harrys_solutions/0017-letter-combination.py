#yay solved it in one go 


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        temp = []
        def dfs(i):
            print(temp)
            # i is the index of the string digits
            if i >= len(digits):
                res.append(''.join(temp))
                return
            # if i > len(digits):
            #     return 

            for l in digits_map[digits[i]]:
                temp.append(l)
                dfs(i+1)
                temp.pop()

            return res 

        return dfs(0)

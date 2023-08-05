class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0  

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# [1,   3,      5,       2,      1]
#       rob1    rob2     n       n+1


# rob1 is max amount you can rob for [1,3]
# rob2 is the max amount you can rob for [1,3,5]
# in th video minutes 6:00-8:00 is the most helpful part
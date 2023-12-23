class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            # making sure we skip duplicate numbers so we don't add duplicates to res
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            two_sum_res = self.twoSum(nums[i + 1 :], target=-n)
            # print(two_sum_res)
            if two_sum_res:
                print(n, two_sum_res)
                for t in two_sum_res:
                    subset = [n] + t
                    res.append(subset)
        return res

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if (
                curSum > target
                or
                # making sure we skip duplicate numbers so we don't add duplicates to res
                # and making sure we don't go out of bounds
                (r + 1 < len(numbers) and numbers[r] == numbers[r + 1])
            ):
                r -= 1
            elif (
                curSum < target
                or
                # making sure we skip duplicate numbers so we don't add duplicates to res
                # and making sure we don't go out of bounds
                (l != 0 and numbers[l] == numbers[l - 1])
            ):
                l += 1

            else:
                res.append([numbers[l], numbers[r]])
                l += 1
                r -= 1
        return res

# run binary search twice


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last_col = [matrix[i][-1] for i in range(len(matrix))]

        print(last_col)
        l, r = 0, len(matrix) - 1
        prev_l = l
        prev_r = r
        t = 0
        # finds which row the target is in
        while l <= r:
            m = (l + r) // 2
            if last_col[m] < target:
                l = m + 1
                prev_l = l - 1
            elif target < last_col[m]:
                r = m - 1
                prev_r = r + 1
            else:
                return True
        # print(prev_l)
        # print(prev_r)

        if target <= last_col[prev_l]:
            res_i = prev_l
        else:
            res_i = prev_r
        print(res_i)

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[res_i][m]:
                r -= 1
            elif target > matrix[res_i][m]:
                l += 1
            else:
                return True
        return False

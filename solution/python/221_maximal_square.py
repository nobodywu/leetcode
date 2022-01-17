from typing import List


class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        '''
        暴力法，超出时间限制
        '''
        max_side = 0
        if None == matrix or 0 == len(matrix):
            return max_side

        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if "1" == matrix[i][j]:
                    # print("1 == matrix[{}][{}]".format(i, j))
                    max_side = max(1, max_side)
                    remained_max_side = min(rows - i, columns - j)

                    # 剩下的最大边范围
                    for k in range(remained_max_side):
                        flag = True
                        if "0" == matrix[i + k][j + k]:
                            # 判断右下角元素
                            flag = False
                            break

                        for m in range(k):
                            # 判断底边和右边，其他位置判断过了
                            if "0" == matrix[i + k][j + m] or "0" == matrix[i + m][j + k]:
                                flag = False
                                break

                        if flag:
                            # k+1即为当前位置的最大正方形
                            max_side = max(max_side, k + 1)
                        else:
                            break

        return max_side * max_side

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        dp[i][j] 代表以 matrix[i][j]为右下角的正方形最大边长
        边界和初始值:
        以第一行和第一列单元格为右下角的正方形最大边长为该单元格的值
        动态方程:
        dp[i][j] = 0, 如果matrix[i][j]不为"1"
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], p[i-1][j-1]) + 1, 如果matrix[i][j]为"1"
        '''
        max_side = 0
        if None == matrix or 0 == len(matrix):
            return max_side

        rows = len(matrix)
        columns = len(matrix[0])

        dp = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if 0 == i or 0 == j:
                    # 边界还是原来的值，需要转换类型
                    dp[i][j] = int(matrix[i][j])
                else:
                    #
                    if "1" == matrix[i][j]:
                        # 上、左、上左去最小后+1
                        dp[i][j] = min(dp[i-1][j],
                                       dp[i][j-1],
                                       dp[i-1][j-1]) + 1

                max_side = max(max_side, dp[i][j])

        return max_side ** 2


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["1", "0", "1", "0", "0"],
                           ["1", "0", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"],
                           ["1", "0", "0", "1", "0"]]))

    print(s.maximalSquare([["0", "1"]]))

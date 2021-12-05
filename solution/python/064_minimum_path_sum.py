from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if 0 == i and 0 == j:
                    # 跳过[0, 0]
                    continue
                elif 0 == i and 0 != j:
                    # 位于第一行的数据，累加第一行前边的数， 即为到达该位置的最小和
                    grid[i][j] += grid[i][j - 1]
                elif 0 == j and 0 != i:
                    # 位于第一列的数据，累加第一列前边的数， 即为到达该位置的最小和
                    grid[i][j] += grid[i - 1][j]
                else:
                    # 中间的数，累加上边和左边最小的数
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])


        return grid[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))
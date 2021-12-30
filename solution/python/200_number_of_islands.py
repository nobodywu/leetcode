from typing import List


class Solution:
    def dfs(self, grid, r, c):
        # deep first search
        # 把相邻的1置位0
        grid[r][c] = 0
        row = len(grid)
        col = len(grid[0])
        for mov in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ii = r + mov[0]
            jj = c + mov[1]

            # print("pos({}, {}), moved({}, {}):".format(r, c, ii, jj))
            if 0 <= ii < row and 0 <= jj < col and grid[ii][jj] == "1":
                # print("在范围内且为1")
                self.dfs(grid, ii, jj)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        row = len(grid)
        col = len(grid[0])

        count = 0
        for i in range(row):
            for j in range(col):
                # print("i, j: ", i, j)
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([["1", "1", "1", "1", "0"],
                        ["1", "1", "0", "1", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"]]))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化边界，边界全为1
        # 第一个子列表为[1] * n
        # 其他子列表为m - 1个[1] + [0] * (n - 1)
        paths = [[1] * n] + [[1] + [0] * (n - 1) for i in range(m - 1) ]
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[m - 1][n - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
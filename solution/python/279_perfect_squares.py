class Solution:
    def numSquares(self, n: int) -> int:
        '''
        动态规划方法，耗时较高
        '''
        if n < 0:
            return

        if 0 == n:
            return 0

        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i] = i
            j = 1  # 遍历从1到j^2，更新dp[i]
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)  # 1代表j的平方数
                j += 1

        return dp[-1]

    def numSquares2(self, n: int) -> int:
        '''
        数学方法，使用四平方和定理，待研究和补充
        '''
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        动态规划方法求解
        '''
        if 1 == n:
            return 1

        if 2 == n:
            return 2

        ans = [1, 2] + [0] * (n - 2)

        # 爬到第n节台阶有f(n) = f(n - 1) + f(n - 2)种方法
        for i in range(2, n):
            ans[i] = ans[i - 1] + ans[i - 2]

        return ans[-1]

    def climbStairs2(self, n: int) -> int:
        '''
        动态规划方法求解，不使用数组
        '''
        a, b, c = 0, 0, 1
        for i in range(n):
            a = b
            b = c
            c = a + b

        return c

    def climbStairs3(self, n: int) -> int:
        '''
        数学方法求解
        '''
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(2))
    print(s.climbStairs2(3))
    print(s.climbStairs2(4))
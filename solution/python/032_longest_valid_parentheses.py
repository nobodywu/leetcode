class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)

        if length <= 1:
            return 0

        # 初始化一个长度为length的数组
        dp = [0] * length

        for i in range(length):
            if s[i] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                # 如果i - dp[i - 1] -2为-1，根据初始化，dp最后一个元素为0，因此无影响
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] -2] + 2

        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()())"))
    print(s.longestValidParentheses("(()())))()()((()()()()"))

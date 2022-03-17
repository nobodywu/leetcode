class Solution:
    def countSubstrings(self, s: str) -> int:
        # 使用动态规划求解
        # dp[i][j]代表子串s[i:j]是否是回文子串
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left < 2 or dp[left + 1][right - 1]):

                    dp[left][right] = True
                    count += 1

        print(dp)
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aaa"))

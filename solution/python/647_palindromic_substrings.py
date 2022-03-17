class Solution:
    def countSubstrings(self, s: str) -> int:
        # 使用动态规划求解
        # dp[i][j]代表子串s[i:j]是否是回文子串
        # 存在以下几种情况
        # 1. 子串长度为1，可以根据s[i] == s[j]判断是否为回文
        # 2. 子串长度为2，可以根据s[i] == s[j]判断是否为回文
        # 3. 子串长度大于2，在s[i] == s[j] & dp[left + 1][right - 1]进行判断
        # 第三种情况要求，在遍历右侧index为j的时候，要把右侧index为j - 1的情况枚举完
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left < 2 or dp[left + 1][right - 1]):

                    dp[left][right] = True
                    count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aaa"))

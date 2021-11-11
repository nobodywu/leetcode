class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        中心扩展法
        '''
        start, end =0, 0
        for i in range(len(s)):
            left1, right1 = self.expandIndex(s, i, i)
            left2, right2 = self.expandIndex(s, i, i + 1)
            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]


    def expandIndex(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

if __name__== "__main__":
    s = Solution()
    print(s.longestPalindrome("ababc"))
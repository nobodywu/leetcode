from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n, ans = len(s), len(p), []

        if m < n:
            return ans

        # 初始化字符统计数组为0，大小为字母个数（26）
        s_count = [0] * 26
        p_count = [0] * 26
        # ord函数返回字符的ASCII编码值，ord("a") = 97
        # 窗口大小为n，先判断s的前n个字符是否与p相等
        for i in range(n):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(p[i]) - ord("a")] += 1

        if s_count == p_count:
            ans.append(0)

        # 在字符串s上，窗口向右滑动
        for i in range(n, m):
            # 每移动一位，要减小前面字符计数
            s_count[ord(s[i - n]) - ord("a")] -= 1
            # 增加后面字符计数
            s_count[ord(s[i]) - ord("a")] += 1

            if s_count == p_count:
                # 当前窗口的起始位置为i - n + 1
                ans.append(i - n + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams(s="cbaebabacd", p="abc"))

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        动态规划
        word1 长度为 m
        word2 长度为 n
        初始化数组长度为 (m + 1) * (n + 1)
        e 5
        s 4
        r 3
        o 2
        h 1
        # 0 1 2 3
          # r o s
        最短编辑距离为D[i][j]，状态转移方程:
        当word1[i - 1] != word2[j - 1] 且 i != 0 且 j != 0，D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
        当word1[i - 1] == word2[j - 1] 且 i != 0 且 j != 0，D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1] - 1)  
        '''
        m = len(word1)
        n = len(word2)

        if 0 == n:
            return m
        
        if 0 == m:
            return n

        ans = [[0] * (n + 1) for _ in range(m + 1)]
        # print(ans)

        for i in range(1, m + 1):
            ans[i][0] = i

        for i in range(1, n + 1):
            ans[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] != word2[j - 1]:
                    ans[i][j] = 1 + min(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1])
                else:
                    ans[i][j] = 1 + min(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1] - 1)

        return ans[i][j]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))
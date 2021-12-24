from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        步骤：
        1. 初始化dp数组，长度为len(s) + 1，值为False
        2. dp[0]代表空字符，设置值为True
        3. 遍历s中的字符串：
           循环i，区间为[0, len(s)]：
               循环j，区间为[i + 1, len(s)]:
                   如果dp[i] 为 True 且 dp[i:j] 在 wordDict 中，则dp[j] 为 True。说明s[0:j]都可以使用wordDict表示

        dp     0     1    2    3    4    5    6    7    8
        s      ""    l    e    e    t    c    o    d    e
        T/F    T     F    F    F    T    F    F    F    T
        '''
        size = len(s)
        dp = [True] + [False] * size 

        for i in range(size + 1):
            for j in range(i + 1, size + 1):
                print(i, j, s[i:j])
                if dp[i] and s[i:j] in wordDict:
                    print("true")
                    dp[j] = True

        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
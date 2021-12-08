from typing import Collection

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)

        for ch in t:
            need[ch] += 1 # t可能包含重复字符

        first, last = 0, 0
        ans = []

        # 第一步，移动last，直到包含了所有t
        for last, v in enumerate(s):
            # print(first, last, v, need, ans)
            if v in need.keys():
                need[v] -= 1

            # need.values() <= 0说明当前[first, last]区间内包含了所有t
            # 第二步，移动first，移除左侧不包含t中的字符
            if max(need.values()) <= 0:
                while True:
                    # print("移动first", first)
                    if s[first] in need.keys():
                        if need[s[first]] != 0:
                            # 说明当前[first, last]区间内字符s[first]的个数比t多
                            need[s[first]] += 1
                        else:
                            # 更新最小区间
                            if 0 == len(ans):
                                ans = [first, last]
                            if ans[1] - ans [0] > last - first:
                                ans = [first, last]
                            break
                    first += 1

                # 现在s[first]是最小区间位置，移动first继续向后寻找
                need[s[first]] += 1
                first += 1


        if 0 == len(ans):
            return ''
        else:
            return s[ans[0]:ans[1] + 1]


if __name__ == "__main__":
    s = Solution()
    # print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("aa", "aa"))
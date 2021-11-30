from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 初始化一个值为list类型的dict
        ans = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        # [ans.values()]没有将对象进行转换
        return list(ans.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
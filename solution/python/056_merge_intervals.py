from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 使用lambda表达式将数组按照每个子列表中的第一个元素进行排序
        intervals.sort(key = lambda x: x[0])

        ans = []

        for each in intervals:
            if not ans or ans[-1][-1] < each[0]:
                ans.append(each)
            else:
                ans[-1][1] = max(ans[-1][1], each[1])

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
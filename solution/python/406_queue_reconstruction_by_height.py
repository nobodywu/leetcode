from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先对身高进行排序：
        # 1. 对身高按照降序排列；
        # 2. 对相同身高下，身高大于或等于这个身高的人数按升序排列（为了保证后续插入的正确性）
        # 使用lambda表达式进行满足上述两个条件的排序
        people = sorted(people, key=lambda p: (-p[0], p[1]))

        # 以下不能保证条件2
        # people = sorted(people, key = lambda p:(p[0], p[1]), reverse = True)
        # people = sorted(people, reverse = True)

        ans = []
        for p in people:
            if len(ans) <= p[1]:
                # 目前的人数不够或相等
                ans.append(p)
            else:
                # 目前的人数多了，那么就在p[1]的位置插入p
                ans.insert(p[1], p)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

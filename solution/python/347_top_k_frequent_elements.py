from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return

        # 用dict统计数组中各个元素出现的次数
        a = {}
        for each in nums:
            if each not in a.keys():
                a[each] = 1
            else:
                a[each] += 1
        # 字典排序。按照key排序，按照value排序，对列表中的字典元素排序：
        # https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html
        # 按字典的元素进行排序
        # 对字典中的items进行排序, dict.items()返回一个列表，列表元素为key-value对
        # sorted排序的对象为(value, key)，引入lambda进行构造
        # 返回的还是(key, value)
        sorted_a = sorted(a.items(), key=lambda aitm: (aitm[1], aitm[0]), reverse=True)
        # print(sorted_a)
        ans = []
        for i in range(k):
            ans.append(sorted_a[i][0])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))

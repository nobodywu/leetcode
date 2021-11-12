class Solution:
    def twoSum1(self, nums: list, target: int) -> list:

        for i, v1 in enumerate(nums):

            for j, v2 in enumerate(nums):
                if i == j:
                    continue

                if v1 + v2 == target:
                    return [i, j]

    def twoSum2(self, nums: list, target: int) -> list:

        nums_length = len(nums)

        for i in range(nums_length):
            # if i + 1 != nums_length:
            # 不需要考虑i + 1 是否等于 len(height)，range(5,5)为空
            for j in range(i + 1, nums_length):

                if nums[i] + nums[j] == target:
                    return [i, j]



    def twoSum3(self, nums: list, target: int) -> list:
        '''
        使用字典，**求解速度最快**。
        首先遍历一次，构造字典，列表中元素为字典key，列表的index为字典的value
        再一次遍历，根据目标值和当前列表元素值只差，获取对应字典的value（即为index）
        如果dict.get()的返回值不为Node且返回值不等于当前遍历的index，则输出结果
        '''

        a = {}
        for i, v in enumerate(nums):
            a[v] = i

        for i, v in enumerate(nums):
            diff_index = a.get(target-v)

            if diff_index is not None and diff_index != i:
                return [i, diff_index]

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum1([6,7,4], 11))
    print(s.twoSum2([3,9,1], 4))
    print(s.twoSum3([2,7,10], 9))

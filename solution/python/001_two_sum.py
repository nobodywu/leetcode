class Solution:

    '''遍历'''

    def twoSum1(self, nums: list, target: int) -> list:
        # 依次遍历nums的元素，nums[i]，i属于[0, len(nums))
        #     - 对于每个nums[i]，依次遍历nums[j]，j属于[i + 1, len(nums))
        #         - 判断nums[i] + nums[j] 是否等于 target，如果是则返回下标
        # 时间复杂度O(N^2)
        # 空间复杂度O(1)

        nums_length = len(nums)

        for i in range(nums_length):
            # 不需要考虑i + 1 是否等于 len(height)，range(5,5)为空
            for j in range(i + 1, nums_length):

                if nums[i] + nums[j] == target:
                    return [i, j]

    '''
    哈希
    使用Python字典，字典通过哈希实现，因此查找key是否在dict中的时间复杂度为O(1)
    '''

    def twoSum2(self, nums: list, target: int) -> list:
        # 采用两次遍历
        # 第一次遍历构造字典，以num为key，index为value
        # 第二次遍历时，判断target - num是否在字典的key中
        #     - 如果是，返回[当前索引，dict.get(target - num)]
        # 时间复杂度O(N)
        # 空间复杂度O(1)

        a = {}
        for i, num in enumerate(nums):
            a[num] = i

        for i, num in enumerate(nums):
            # 如果key不存在，dict.get()将返回None
            diff_index = a.get(target - num)

            if diff_index is not None and diff_index != i:
                return [i, diff_index]

    def twoSum3(self, nums: list, target: int) -> list:
        # 优化，采用一次遍历
        # 遍历时，先判断target - num是否在字典的key中
        #     - 如果是，返回[当前索引，dict.get(target - num)]
        # 然后构造字典。
        # 注意：因为不可以使用重复的元素，构造字典要在判断之后
        # 时间复杂度O(N)
        # 空间复杂度O(1)

        a = {}
        for i, num in enumerate(nums):
            diff_index = a.get(target - num)

            if diff_index is not None and diff_index != i:
                return [i, diff_index]

            a[num] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum1([6, 7, 4], 11))
    print(s.twoSum2([3, 9, 1], 4))
    print(s.twoSum3([2, 7, 10], 9))

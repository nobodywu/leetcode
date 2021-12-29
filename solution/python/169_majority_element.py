from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        size = len(nums)
        nums_dict = {}

        for i in range(size):
            if nums[i] in nums_dict.keys():
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        # 两种遍历dict中key的写法
        # for key in nums_dict:
        #     print(key)
        # for key in nums_dict.keys():
        #     print(key)

        # 遍历dict中的key-value对
        for key, value in nums_dict.items():
            if value > size / 2:
                return key

    def majorityElement2(self, nums: List[int]) -> int:
        '''
        list sort函数时间复杂度：O(nlogn)。
        list sort函数空间复杂度：O(logn)。
        '''
        nums.sort()
        # nums = [3, 2, 3] 3 // 2 = 1，索引从0开始，无需再 + 1
        return nums[len(nums) // 2]


if __name__ == "__main__":
    s = Solution()
    # 传入的nums一定有多数元素，多数元素为元素个数大于len(nums)/2的元素
    print(s.majorityElement2([3, 2, 3]))
    print(s.majorityElement2([3]))

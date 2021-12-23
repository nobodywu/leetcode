from typing import List
from functools import reduce

class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        nums.sort()

        if 1 == len(nums):
            return nums[0]

        for i in range(len(nums)):

            if i == 0:
                if nums[i] == nums[i + 1]:
                    continue
                else:
                    return nums[i]

            if i == len(nums) - 1:
                if nums[i - 1] == nums[i]:
                    continue
                else:
                    return nums[i]

            if nums[i] == nums[i + 1] or nums[i - 1] == nums[i]:
                continue
            else:
                return nums[i]

    def singleNumber2(self, nums: List[int]) -> int:
        '''
        使用异或运算
        1. 任何数和 00 做异或运算，结果仍然是原来的数，即 a ^ 0 = a
        2. 任何数和其自身做异或运算，结果是0，即 a ^ a = 0
        3. 异或运算满足交换律和结合律，即 a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b

        reduce:
        https://www.runoob.com/python/python-func-reduce.html
        '''
        return reduce(lambda x, y: x ^ y, nums)

if __name__=="__main__":
    s = Solution()
    print(s.singleNumber2([4,1,2,1,2]))

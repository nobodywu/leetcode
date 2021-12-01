from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pre, max_sum = 0, 0
        for i in range(len(nums)):
            # 如果累加值加上当前数字比当前数字小，那么把前边的累加丢掉，使用当前数子
            pre = max(pre + nums[i], nums[i])
            max_sum = max(max_sum, pre)

        # max_sum不可能小于0
        if 0 == max_sum:
            return max(nums)
        else:
            return max_sum

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([-2]))
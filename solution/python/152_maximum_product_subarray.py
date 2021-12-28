from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return

        min_i, max_i, max_product = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            t_max_i, t_min_i = max_i, min_i
            # 类似第53题，累积的时候要和当前nums[i]进行比较
            # 用min_i进行负值情况的考虑
            max_i = max(t_min_i * nums[i], nums[i], t_max_i * nums[i])
            min_i = min(t_min_i * nums[i], nums[i], t_max_i * nums[i])

            max_product = max(max_product, max_i)

        return max_product


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
    # 最大子串为[5, 6, -3, 4, -3]，而不是[5, 6]，累积的时候要考虑负值
    print(s.maxProduct([5, 6, -3, 4, -3]))

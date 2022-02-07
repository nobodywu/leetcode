from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        # 统计非0元素个数
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]  # 将非0元素按顺序放入nums数组
                j += 1

        # 在数组末尾补0
        for i in range(j, len(nums)):
            nums[i] = 0

        return nums


if __name__ == "__main__":
    nums = [0, 1, 5, 6, 0, 9]
    s = Solution()
    print(s.moveZeroes(nums))

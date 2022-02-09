from typing import List


class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        '''
        使用字典求解，空间复杂度不符合题目要求的O(1)
        '''
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict.keys():
                return nums[i]

            nums_dict[nums[i]] = i

    def findDuplicate(self, nums: List[int]) -> int:
        '''
        https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
        二分法查找，空间复杂度O(1)
        '''
        left = 1
        right = len(nums) - 1

        while left < right:
            count = 0
            mid = left + (right - left) // 2  # 猜测一个重复数，向下取整

            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                # 重复数字出现在[left, mid]
                right = mid
            else:
                # 重复数字出现在[mid + 1, right]
                left = mid + 1

        return left  # left == right


if __name__ == "__main__":
    s = Solution()
    # 题目中假设只存在一个重复数字
    print(s.findDuplicate([2, 3, 4, 5, 1, 6, 2]))

from typing import List


class Solution:
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        # 将数组看做是三个子数组构成，numsa, numsb, numsc
        # 将nums进行升序排序后得到nums_sorted
        # nums与nums_sorted数组前边相同的数组即为numsa
        # 后边相同的数组即为numsc
        # 中间部分即为符合题意的最短子数组numsb
        if not nums:
            return

        length = len(nums)

        # 如果数组长度为1
        if length == 1:
            return 0

        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False

            return True

        # 如果数组已经按照升序排列
        if is_sorted(nums):
            return 0

        nums_sorted = sorted(nums)

        left, right = 0, length - 1

        while True:
            if nums[left] != nums_sorted[left]:
                break

            left += 1

        while True:
            if nums[right] != nums_sorted[right]:
                break

            right -= 1

        return right - left + 1
        # return len(nums[left:right + 1])

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        # 一次遍历
        length = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(length):
            # 从左向右，寻找右边界，右边界为最后一个比maxn小的元素
            # 等于的时候不能更新right
            if nums[i] >= maxn:
                maxn = nums[i]
            else:
                right = i

            # 从右向左，寻找左边界，右边界为最后一个比minn大的元素
            # 等于的时候不能更新left
            if nums[length - 1 - i] <= minn:
                minn = nums[length - 1 - i]
            else:
                left = length - 1 - i

        # 如果left == right == -1 说明数组是升序排列的
        return right - left + 1 if right != -1 else 0


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray2([2, 6, 4, 8, 10, 9, 15]))
    print(s.findUnsortedSubarray2([1, 2, 3, 3, 3]))

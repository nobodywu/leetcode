from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        if not nums and 0 == len(nums):
            return

        length = len(nums)

        left = [0 for _ in range(length)]
        right = [0 for _ in range(length)]
        answer = [0 for _ in range(length)]

        # 左侧乘积边界，第一个元素为1（左侧没有其他元素）
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]

        # 右侧乘积边界，最后一个元素为1（右侧没有其他元素）
        right[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        if not nums and 0 == len(nums):
            return

        length = len(nums)

        left = [0 for _ in range(length)]
        answer = [0 for _ in range(length)]

        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]

        # 用变量right取代right数组，降低空间复杂度
        right = 1
        answer[length - 1] = left[length - 1]  # 边界单独赋值
        for i in range(length - 2, -1, -1):
            right = nums[i + 1] * right
            answer[i] = left[i] * right

        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf2([1, 2, 3, 4]))

from typing import List


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)

        for i in range(len(nums) - 1, -1, -1):
            # print(i, k)
            if 1 == k:
                return nums[i]

            k -= 1

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return nums[k - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest1(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(s.findKthLargest2(nums=[3, 2, 1, 5, 6, 4], k=2))

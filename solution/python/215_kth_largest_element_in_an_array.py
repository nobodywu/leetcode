from typing import List
from algo import heap_sort


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

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        heap_sort.heapSort(nums)

        return nums[-k]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest1(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(s.findKthLargest2(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(s.findKthLargest3(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(s.findKthLargest3(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))

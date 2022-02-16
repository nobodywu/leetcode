from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        动态规划法，时间复杂度O(n^2)
        方程：
        dp[i] = max(dp[i], dp[j] + 1), 
        其中：
        1. i in [0, len(nums)]
        2. j in [0, i] 且 nums[j] < nums[i]
        '''

        if not nums:
            return

        dp = list()

        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))

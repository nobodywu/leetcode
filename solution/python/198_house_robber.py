from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        动态规划
        100    0    0    100

        1. 第一间房子，dp[0] = nums[0]
        2. 第二间房子，dp[1] = max(nums[0], nums[1])
        3. 后面的房子，dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        '''
        if not nums:
            return

        size = len(nums)

        if 0 == size:
            return 0

        if 1 == size:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([100, 0, 0, 100]))
    print(s.rob([1, 2, 3, 1]))

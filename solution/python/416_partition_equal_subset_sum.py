from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 动态规划问题，0-1背包问题
        # 如果一个数组可以拆分成两个元素和相等的子集，那么这个数组的和一定是偶数
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)
        length = len(nums)

        # 可以优化dp数组为一维数组
        dp = [[False for _ in range(target + 1)] for _ in range(length)]

        # dp[i][j]表示在闭区间[0, i]内，挑选一些元素使其总和为j
        for i in range(length):
            for j in range(target + 1):
                if j == 0:
                    # 第一列，任何一个区间内，都可以使总和为0（不选元素）
                    # 第一列无意义
                    dp[i][j] = True
                    continue

                if nums[i] > j:
                    # 那么需要看在区间[0, i-1]内挑选元素总和能不能为j，即为集成之前的状态，这也是为什么可以优化dp为一维数组的原因
                    dp[i][j] = dp[i - 1][j]
                    continue

                if nums[i] == j:
                    # 选取当前元素可以达到总和j
                    dp[i][j] = True
                    continue

                if nums[i] < j:
                    # 当前元素比总和j小
                    # 那么需要看在区间[0, i-1]内挑选元素总和能不能为j
                    # 或者在区间[0, i-1]内挑选元素总和能不能为j-nums[i]
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]

        return dp[-1][-1]


if __name__ == "__main__":

    s = Solution()
    print(s.canPartition([1, 5, 10, 6]))

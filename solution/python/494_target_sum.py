from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        动态规划求解，完全背包问题，所有元素都要取
        定义dp[i][j]为，对nums区间[0, i]内所有元素进行+-操作，和为j的方法数
        '''
        # nums的元素为非负整数，对所有元素进行+-操作的范围为[-sum, sum]
        # 因此dp数组的大小应该为 len(nums) * (sum(nums) * 2 + 1)
        nums_sum = sum(nums)

        if nums_sum < target:
            return 0

        dp = [[0 for _ in range(nums_sum * 2 + 1)] for _ in range(len(nums))]

        # 初始化dp数组第一行
        # 取元素nums[0]进行+-，可以使目标和为-num[0]和num[0]
        # 因此设置dp[0][sum - num[0]]和dp[0][sum + num[0]]的方法数为1
        # sum的位置dp[0][sum]代表和为0
        # nums_sum - nums[0] 可能与 nums_sum + nums[0] 相同，因此是+=
        dp[0][nums_sum - nums[0]] += 1
        dp[0][nums_sum + nums[0]] += 1

        # 从nums[1]开始
        for i in range(1, len(nums)):
            for j in range(-nums_sum, nums_sum + 1):
                # j的范围为[-nums_sum, nums_sum + 1)
                # 元素和为j，对应的索引为j + nums_sum
                if j - nums[i] < -nums_sum:
                    # -num[i]超出了范围
                    # 只能由上一个元素和为j + num[i]的状态转移而来，索引为dp[i - 1][j + nums_sum + num[i]]
                    dp[i][j + nums_sum] = dp[i - 1][j + nums_sum + nums[i]]

                elif j + nums[i] > nums_sum:
                    # +num[i]超出了范围
                    # 只能由上一个元素和为j - num[i]的状态转移而来，索引为dp[i - 1][j + nums_sum - num[i]]
                    dp[i][j + nums_sum] = dp[i - 1][j + nums_sum - nums[i]]

                else:
                    # 可以由上一个元素和为j - num[i]和j + num[i]的状态转移而来
                    dp[i][j + nums_sum] = dp[i - 1][j + nums_sum + nums[i]] + dp[i - 1][j + nums_sum - nums[i]]

        return dp[-1][target + nums_sum]


if __name__ == "__main__":
    # nums[i] 为自然数（非负整数）
    s = Solution()
    # print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
    # print(s.findTargetSumWays([1], 2))
    print(s.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))

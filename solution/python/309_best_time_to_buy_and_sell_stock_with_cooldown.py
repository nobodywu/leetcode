from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 规则：1. 在买入前不能持有；2. 卖出后的第二天不能买入
        # profits[i][0]表示现在有股票，卖出，结果无股票，且第二天不能买入。可以由profits[i-1][1]，profits[i-1][3]迁入
        # profits[i][1]表示现在有股票，不卖，结果有股票。可以由profits[i-1][1]，profits[i-1][3]迁入
        # profits[i][*]表示现在有股票，买入，不存在这种情况，有股票不可以再买
        # profits[i][*]表示现在无股票，卖出，不存在这种情况
        # profits[i][2]表示现在无股票，不卖，结果无股票。可以由profits[i-1][0]，profits[i-1][2]迁入
        # profits[i][3]表示现在无股票，买入，结果有股票。profits[i-1][2]迁入

        profits = [[0] * 4 for _ in range(len(prices))]
        # print(profits)

        profits[0][0] = float("-inf")  # 第0天无这种情况
        profits[0][1] = float("-inf")   # 第0天无这种情况
        profits[0][2] = 0   # 第0天无股票，不卖
        profits[0][3] = -prices[0]  # 第0天无股票，买入

        for i in range(1, len(prices)):
            # print(i)
            profits[i][0] = max(profits[i-1][1], profits[i-1][3]) + prices[i]
            profits[i][1] = max(profits[i-1][1], profits[i-1][3])
            profits[i][2] = max(profits[i-1][0], profits[i-1][2])
            profits[i][3] = profits[i-1][2] - prices[i]
            # print(profits)

        return max(profits[-1][0], profits[-1][1], profits[-1][2], profits[-1][3])


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
    print(s.maxProfit([1]))
    print(s.maxProfit([1, 2]))

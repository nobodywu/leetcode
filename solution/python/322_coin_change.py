from typing import List
from functools import lru_cache


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        '''
        记忆化，依次分解，求子问题总数最小
        '''

        # 总金额amount下的最小个数
        @lru_cache(amount)
        def mini_count_in(amount_):
            if amount_ < 0:
                return -1

            if amount_ == 0:
                return 0

            mini_count = float("inf")
            for coin in self.coins:
                sub_mini_count = mini_count_in(amount_ - coin)

                # 如果子最小个数比前一种情况的当前amount的最小个数还小，那么更新当前amount的最小个数
                if sub_mini_count >= 0 and sub_mini_count < mini_count:
                    mini_count = sub_mini_count + 1  # 当前amount的最小个数

            return mini_count if mini_count < float("inf") else -1

        if amount < 0:
            return -1

        if amount == 0:
            return 0

        self.coins = coins
        return mini_count_in(amount)


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange1([2, 5, 10, 1], 27))

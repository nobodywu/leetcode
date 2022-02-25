from typing import List
from functools import lru_cache


class Solution:
    def maxCoins1(self, nums: List[int]) -> int:
        # 记忆化搜索，采用分治法，向中间插入气球
        val = [1] + nums + [1]

        # 函数装饰器@functools.lru_cache()，可以让之前的计算结果保存下来，不被置换出去，在之后再用到相同的调用直接返回结果，提供类似记忆化的功能
        # https://www.cnblogs.com/zikcheng/p/14322577.html
        @lru_cache(None)
        def solve(left, right):
            if left >= right - 1:
                return 0

            # 每种可能下的best
            best = 0
            # 遍历left和right之间的nums元素，依次向中间插入气球
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                # 继续在left和i，i和right之间插入气球
                total += solve(left, i) + solve(i, right)
                best = max(best, total)

            return best

        # 初始的left值为为val[0]，right值为为val[-1]
        return solve(0, len(nums) + 1)

    def maxCoins2(self, nums: List[int]) -> int:
        '''
        动态规划
        https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
        '''
        if not nums:
            return

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0] * nums[1] + nums[1], nums[0] + nums[0] * nums[1])

        # 补充前后边界
        nums = [1] + nums + [1]

        scores = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # 表示开区间(i, j)内的最大得分
        def best_score_in_range(i, j):
            # 计算在区间(i, j)内戳破*最后一只*气球k的最大得分
            best_score = 0
            for k in range(i + 1, j):
                left = scores[i][k]
                right = scores[k][j]
                cur_score = left + nums[i] * nums[k] * nums[j] + right

                if cur_score > best_score:
                    best_score = cur_score

            scores[i][j] = best_score

        # 区间从3到最大依次循环，最大区间为len(nums)，nums是补充前后边界后的数组
        for section in range(3, len(nums) + 1):
            for i in range(0, len(nums) - section + 1):
                j = i + section - 1
                best_score_in_range(i, j)

        # 返回最大区间的得分(0, len(nums) - 1)，nums是补充前后边界后的数组
        return scores[0][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins2([3, 1, 5, 8]))

    '''
    对nums的边界补1
    1, 3, 1, 5, 8, 1
    
    dp 数组，大小为 (len(nums) + 2) * (len(nums) + 2)，6 * 6
    0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0
    '''

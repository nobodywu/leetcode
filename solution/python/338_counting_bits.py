from typing import List


class Solution:
    def countBits1(self, n: int) -> List[int]:
        '''
        Brian Kernighan算法，通过x & (x - 1)运算依次消去末尾1

        7        111 & 110 = 110 消去末尾1
        6        110 & 101 = 100 消去末尾1
        ...

        '''

        def count_ones(x):
            count = 0

            while x > 0:
                x = x & (x - 1)
                count += 1

            return count

        return [count_ones(x) for x in range(n + 1)]

    def countBits2(self, n: int) -> List[int]:
        '''
        动态规划，高位，取2的整数次幂为high_bit，并依次更新high_bit值
        对于x，一比特个数为dp[x - high_bit] + 1，比前一个2的整数次幂段多一
        '''

        dp = [0]
        high_bit = 0
        for x in range(1, n + 1):
            # x & (x - 1)为0则说明x为2的整数次幂（最有最高位为1）
            if x & (x - 1) == 0:
                high_bit = x

            dp.append(dp[x - high_bit] + 1)

        return dp


if __name__ == "__main__":
    '''
    十进制     二进制
    0              0
    1             01
    2             10
    3             11
    4            100
    5            101
    6            110
    7            111
    '''
    s = Solution()
    print(s.countBits1(7))
    print(s.countBits2(7))

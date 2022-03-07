class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        # 取异或运算
        res = x ^ y

        def count_ones(a):
            '''
            Brian Kernighan算法，问题338
            依次去掉末尾1
            '''
            count = 0
            while a > 0:
                a = a & (a - 1)
                count += 1

            return count

        return count_ones(res)


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1, 4))

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        子集可以与二进制数对应起来
        binary    subset    decimal
        000       []        0
        001       [3]       1
        010       [2]       2
        011       [2, 3]    3
        100       [1]       4
        101       [1, 3]    5
        110       [1, 2]    6
        111       [1, 2, 3] 7
        '''
        ans = []

        # 生成 0 到 (2 ^ n - 1)的十进制数 decimal number
        # binary number
        for dec in range(2**len(nums)):
            comb_bina = [0] * len(nums)
            idx = len(nums) - 1
            combination = []
            # 计算十进制数对应的二进制数
            while True:
                quotient = dec // 2
                remainder = dec % 2
                comb_bina[idx] = remainder
                if 0 == quotient:
                    break

                idx -= 1
                dec = quotient

            for i, v in enumerate(comb_bina):
                if v != 0:
                    combination.append(nums[i])

            # print(comb_bina)
            # print(combination)
            ans.append(combination)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
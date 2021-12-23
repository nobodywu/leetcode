from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_size = 0
        nums_set = set(nums)

        for num in nums_set:
            # print(num)
            # 如果num - 1 在nums_set中，这种情况在num为更小的数的时候考虑过了
            if num - 1 not in nums_set:
                current_size = 1

                while num + 1 in nums_set:
                    current_size += 1
                    num += 1

                longest_size = max(longest_size, current_size)

            #     print("当前连续为{}，最长连续为{}".format(current_size, longest_size))
            # else:
            #     print("没有连续")

        return longest_size


if __name__=="__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
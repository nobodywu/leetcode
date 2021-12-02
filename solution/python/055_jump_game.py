from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0
        size = len(nums)

        if 1 == size:
            # nums为非负
            return True

        for i in range(size - 1):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])

                if size - 1 <= right_most:
                    return True

        return False

        # return False

if __name__ == "__main__":
    s = Solution()
    # print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    # print(s.canJump([1,0,1,0]))
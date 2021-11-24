class Solution:
    def searchRange1(self, nums: list, target: int) -> list:
        ans = [-1, -1]
        length = len(nums)

        if not nums:
            return ans

        for i in range(length):
            if nums[i] == target:
                ans[0] = i
                break

        for j in range(length):
            idx = length - j - 1
            if nums[idx] == target:
                ans[1] = idx
                break

        return ans

    def searchRange2(self, nums: list, target: int) -> list:
        '''
        二分法的时间复杂度为log(n)
        '''
        l, r = 0, len(nums) - 1

        # 将nums分为[0, mid]和[mid + 1, length]
        # 查找最左
        while l < r:
            mid = (l + r) // 2 # 每次都取最左边

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[r] != target:
            return [-1, -1]

        L = r

        l, r = 0, len(nums) - 1

        # 查找最右
        while l < r:
            mid = (l + r) // 2 + 1 # 每次都取最右边

            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        return [L, r]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange2([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange2([0, 3], 0))
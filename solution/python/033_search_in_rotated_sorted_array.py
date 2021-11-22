class Solution:
    def search1(self, nums: list, target: int) -> int:
        if nums and target in nums:
            return nums.index(target)
        else:
            return -1

    def search2(self, nums: list, target: int) -> int:
        '''
        二分法

        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环. 
        '''
        if not nums:
            return -1

        m, n = 0, len(nums) - 1

        while m <= n:
            mid = (m + n) // 2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                # 左边[0, mid]是有序的
                if nums[0] <= target < nums[mid]:
                    # target在左边，更新右边界
                    n = mid - 1
                else:
                    # target在右边，更新左边界
                    m = mid + 1
            else:
                # 右边[mid + 1, n]是有序的
                if nums[mid] < target <= nums[n]:
                    # target在右边，更新左边界
                    m = mid + 1
                else:
                    # target在左边，更新右边界
                    n = mid - 1

        return -1 
                

if __name__ == "__main__":
    s = Solution()
    print(s.search2([4, 5, 6, 0, 1, 2], 3))
    print(s.search2([4, 5, 6, 0, 1, 2], 2))
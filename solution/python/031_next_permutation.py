class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
        
        步骤：
        1. 从后向前查找第一个升序的数对，nums[i]和nums[j],5和7
        2. 查找nums[i]以后，从后往前第一个比nums[i]大的数（也是nums[i]以后的所有比nums[i]大的数中最小的数），nums[k]
        3. 交换nums[i]和nums[k]
        4. 交换后，nums[j:]必为降序，按照升序排列nums[j:]
        """
        length = len(nums)
        # if 0 == length:
        #     return

        # if 1 ==length:
        #     return nums

        # 如果长度为1，返回空也是正确的，因为nums=[1]本身就存在，不需要排序
        if 1 >=  length:
            return

        i, j, k = length - 2, length - 1, length - 1

        # 找到nums[i], nums[j]
        while i >= 0 and nums[i] >= nums[j]: # 需要比较nums[0],nums[1]
            i -= 1
            j -= 1

        # 找到nums[k]
        if i >= 0: # 上个while中不存在nums[i] < nums[j]时，i为-1，j为0，此时为最大组合，不需要交换
            while nums[i] >= nums[k]:
                k -= 1

            # 交换
            nums[i], nums[k] = nums[k], nums[i]

        # 从小到大重排nums[j:end], [1, 2, 3, 8, 6, 8, 7, 5, 4]
        end = length - 1
        while j < end:
            nums[j], nums[end] = nums[end], nums[j]
            j += 1
            end -= 1

        return nums


if __name__=="__main__":
    s = Solution()
    print(s.nextPermutation([8, 7, 6, 3]))
    print(s.nextPermutation([1, 2, 3, 8, 5, 8, 7, 6, 4]))

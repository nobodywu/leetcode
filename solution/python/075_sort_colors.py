from typing import List

class Solution:
    '''
    nums[i] 为 0、1 或 2
    Do not return anything, modify nums in-place instead.
    '''
    def sortColors(self, nums: List[int]) -> None:
        nums.sort() # list.sort()没有返回值
        return nums

    def sortColors2(self, nums: List[int]) -> None:
        '''
        单指针，两次遍历数组，第一次将所有0替换到前边，第二次将所有1替换到前边
        '''
        idx = 0

        for i in range(len(nums)):
            if 0 == nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1

        for i in range(idx, len(nums)):
            if 1 == nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1

        return nums

    def sortColors3(self, nums: List[int]) -> None:
        '''
        双指针
        '''
        idx0, idx1 = 0, 0

        for i in range(len(nums)):

            # 需要先换1，再换0
            # nums = [1, 0]时，如果先换0，再换1
            # 第一次循环，nums[0] == 1
            # idx1 == 0, i == 0, nums[idx1]和nums[i]交换后nums不变，idx1变为1
            # 第二次循环, nums[1] == 0
            # idx0 ==0, idx1 == 1, i == 0, nums[idx0]和nums[i]交换后nums为[0,1]，
            # idx0 < idx1 nums[idx1]和nums[i]交换nums不变，
            # idx0变为1，idx1变为2
            # 此时nums[1] == 1，进入if 1 == nums[i]分支，导致nums[idx1]越界
            
            if 1 == nums[i]:
                nums[idx1], nums[i] = nums[i], nums[idx1]
                idx1 += 1

            if 0 == nums[i]:
                nums[idx0], nums[i] = nums[i], nums[idx0]

                if idx0 < idx1:
                    # 说明上面的交换，原来的把nums[idx0] == 1 换到了后边nums[i]
                    # 要把现在的nums[i] == 1换到idx1的位置
                    nums[idx1], nums[i] = nums[i], nums[idx1]

                idx0 += 1
                idx1 += 1

        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortColors3([2,0,2,1,1,0]))
    print(s.sortColors3([1,0]))
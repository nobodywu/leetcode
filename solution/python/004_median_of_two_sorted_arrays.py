class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:

        # list的extend和sort方法没有返回值
        nums1.extend(nums2)
        # list.sort(), sorted(list)
        nums1.sort() # python的排序算法为timsort，对任意长度的数组来说是最优的

        if len(nums1)%2 == 0:
            i = len(nums1)//2
            return (nums1[i-1] + nums1[i])/2

        else:
            i = len(nums1)//2
            return nums1[i]

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,8,3],[4,5,6]))
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:

        # 注意list的extend和sort方法没有返回值
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1)%2 == 0:
            i = len(nums1)//2
            return (nums1[i-1] + nums1[i])/2

        else:
            i = len(nums1)//2
            return nums1[i]

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,8,3],[4,5,6]))
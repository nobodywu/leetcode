class Solution:
    def findMedianSortedArrays1(self, nums1: list, nums2: list) -> float:

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

    def findMedianSortedArrays2(self, nums1: list, nums2: list) -> float:

        def getKthEle(k):
            index1, index2 = 0, 0

            while True:
                # 如果上一循环出现下标越界的，则index = new_index1 + 1恰好为数组长度，此时上一循环计算出的k值无意义 
                # 如果为空数组，返回另一个数组的index(0) + k - 1下标值
                if m == index1:
                    return nums2[index2 + k - 1]
                if n == index2:
                    return nums1[index1 + k - 1]

                if 1 == k:
                    return min(nums1[index1], nums2[index2])
                
                # 正常情况
                # 计算当前数组下标
                new_index1 = min(index1 + (k//2 - 1), m-1) # 如果下标越界，则指向数组最后一个
                new_index2 = min(index2 + (k//2 - 1), n-1)

                ele1 = nums1[new_index1] # 取出数组中的元素
                ele2 = nums2[new_index2]

                if ele1 < ele2:
                    k = k - (new_index1 -index1 + 1) # 更新k值
                    index1 = new_index1 + 1 # 数组下标指向下一个位置
                else:
                    k = k - (new_index2 -index2 + 1)
                    index2 = new_index2 + 1


        m = len(nums1)
        n = len(nums2)

        k = (m + n)//2

        if (m + n) % 2 == 0:
            return (getKthEle(k) + getKthEle(k+1))/2

        else:
            return getKthEle(k+1)


if __name__ == "__main__":
    s = Solution()
    # nums1, muns2每个数组内已经排序
    print(s.findMedianSortedArrays2([1,3,8],[4,5,6])) # 中位数为4.5
    print(s.findMedianSortedArrays2([],[1])) # 中位数为1
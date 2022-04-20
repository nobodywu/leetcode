import statistics


class Solution:
    '''
    使用python内置函数sort和median，median函数中使用sort函数。
    sort函数使用timesort方法进行排序
    时间复杂度O(nlogn)
    空间复杂度O(n)

    timesort算法（需要理解）：
    https://en.wikipedia.org/wiki/Timsort
    https://juejin.cn/post/6941004106525835278
    '''

    def findMedianSortedArrays1(self, nums1: list, nums2: list) -> float:
        # 合并两个列表
        # 使用sort方法进行排序
        # 找出中间元素
        #     - 如果合并的列表长度为偶数，中位数为中间两个元素的平均值
        #     - 如果合并的列表长度为奇数，中位数为中间的元素
        # 时间复杂度O((n + m)log(n + m))，n和m分别为nums1和nums2的长度
        # 空间复杂度O(n + m)

        # list的extend和sort方法没有返回值
        nums1.extend(nums2)
        # list.sort(), sorted(list)
        nums1.sort()  # python的排序算法为timsort，对任意长度的数组来说是最优的

        if len(nums1) % 2 == 0:
            i = len(nums1)//2
            return (nums1[i-1] + nums1[i])/2

        else:
            i = len(nums1)//2
            return nums1[i]

    def findMedianSortedArrays2(self, nums1: list, nums2: list) -> float:
        # 函数median的实现与方法1相同

        return statistics.median(nums1 + nums2)

    '''
    二分
    '''

    def findMedianSortedArrays3(self, nums1: list, nums2: list) -> float:
        # 使用二分法找到第k大的元素
        # 每个列表内的元素都已排序

        # 定义函数getKthEle，找到两个数组中的第K大的元素
        # 定义nums1和nums2两个数组的索引起点index1, index2并初始化为0
        # 在死循环(while True)中不断的将k分配到nums1和nums2中未检查部分元素，判断大小后更新k值和index1和2
        #     - 终止条件，如果index1超出nums1边界，那么k代表的元素在nums2中，返回nums2[index2 + k - 1]。注意k表示第k个，-1得到下标值
        #     - 终止条件，如果index2超出nums2边界，那么k代表的元素在nums1中，返回nums1[index1 + k - 1]。注意k表示第k个，-1得到下标值
        #     - 终止条件，如果当前k为1，此时没有到达nums1或2的末尾，k代表的元素为min(nums1当前的index1, nums2当前的index2)
        #     以下为没有达到终止条件的循环，将k分入nums1和2，计算列表新的索引。
        #     - new_index1 = min(index1 + (k // 2 - 1), len(nums1))。注意k表示第k个，-1得到下标值。越界时索引为列表末尾
        #     - new_index2 = min(index2 + (k // 2 - 1), len(nums2))。注意k表示第k个，-1得到下标值。越界时索引为列表末尾
        #     - 比较新索引下的元素大小，然后更新k值和数组索引
        #         - 如果nums1[new_index1] < nums2[new_index2]。说明nums1索引过的数据要舍弃，剩余k值为k - (new_index1 - index1 + 1)。index1指向下一个位置new_index1 + 1
        #         - 如果nums1[new_index1] >= nums2[new_index2]。说明nums2索引过的数据要舍弃，剩余k值为k - (new_index2 - index2 + 1)。index2指向下一个位置new_index2 + 1

        # 时间复杂度O((n + m)log(n + m))，n和m分别为nums1和nums2的长度
        # 空间复杂度O(1)

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
                new_index1 = min(index1 + (k//2 - 1), m-1)  # 如果下标越界，则指向数组最后一个
                new_index2 = min(index2 + (k//2 - 1), n-1)

                ele1 = nums1[new_index1]  # 取出数组中的元素
                ele2 = nums2[new_index2]

                if ele1 < ele2:
                    k = k - (new_index1 - index1 + 1)  # 更新k值
                    index1 = new_index1 + 1  # 数组下标指向下一个位置
                else:
                    k = k - (new_index2 - index2 + 1)
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
    print(s.findMedianSortedArrays2([1, 3, 8], [4, 5, 6]))  # 中位数为4.5
    print(s.findMedianSortedArrays2([], [1]))  # 中位数为1

from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums and 0 == len(nums):
            return

        length = len(nums)
        ans = []

        # python标准库中的heapify函数，先shift up（构建大根堆），后shift down，与215题heapSort函数功能相同与215题heapify函数功能不同
        # 生成从小到大排序的列表，这里对nums的元素加符号，保证heap后最大的元素在q前边
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans.append(-q[0][0])

        for i in range(k, length):
            heapq.heappush(q, (-nums[i], i))
            # 体现移动窗口，如果最大的元素index不在窗口内则需要去除
            while q[0][1] <= i - k:
                heapq.heappop(q)  # heappop弹出最小的元素

            ans.append(-q[0][0])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

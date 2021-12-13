from typing import List

class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        '''
        暴力求解，超时
        '''

        ans = 0
        for left in range(len(heights)):
            # 对每一个left，寻找右侧的最大矩形
            min_height = heights[left]
            for right in range(left, len(heights)): # for right in range(left + 1, len(heights))不能解决测试用例2和3
                min_height = min(min_height, heights[right]) # 高度最小值
                ans = max((right - left + 1) * min_height, ans) # 面积最大值
        return ans

    def largestRectangleArea2(self, heights: List[int]) -> int:
        size = len(heights)
        left = [0] * size
        right = [0] * size

        # 查找当前柱子左侧第一个最小柱子的位置
        stack = []
        for i in range(size):
            # 如果当前柱子比栈顶元素高，那么移除栈顶元素
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            # 当前栈顶元素比栈顶元素低，该栈顶元素就是左侧第一个最小柱子的位置
            left[i] = stack[-1] if stack else -1 # -1的位置不存在
            stack.append(i)

        # 查找当前柱子右侧第一个最小柱子的位置
        stack = []
        for i in range(size - 1, -1, -1):
            # 如果当前柱子比栈顶元素高，那么移除栈顶元素
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            # 当前栈顶元素比栈顶元素低，该栈顶元素就是右侧第一个最小柱子的位置
            right[i] = stack[-1] if stack else size # 计算面积的时候，size - 1是右侧最后一个不比他小的柱子
            stack.append(i)

        # right - 1是右侧最后一个不比他小的柱子
        return max(((right[i] - 1) - left[i]) * heights[i] for i in range(size)) if size > 0 else 0
        

    def largestRectangleArea3(self, heights: List[int]) -> int:
        '''
        单调栈 + 常数优化
        '''
        pass

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea2([2,1,5,6,2,3]))
    print(s.largestRectangleArea2([1]))
    print(s.largestRectangleArea2([0,9]))
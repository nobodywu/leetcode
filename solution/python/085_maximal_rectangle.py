from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        heights = [0] * n # 每行柱子的高度
        max_area = 0

        for row in range(m):
            # 计算每一行的柱子高度
            for col in range(n):
                if '1' == matrix[row][col]:
                    heights[col] += 1
                else:
                    heights[col] = 0

            # 利用leeicode第84题中的单调栈解法
            max_area = max(max_area, self.largestRectangleArea2(heights))

        return max_area

    def largestRectangleArea2(self, heights: List[int]) -> int:
        size = len(heights)
        left = [0] * size
        right = [0] * size

        stack = []
        for i in range(size):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(size - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else size
            stack.append(i)

        return max(((right[i] - 1) - left[i]) * heights[i] for i in range(size)) if size > 0 else 0



if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    '''
    10100
    10111
    11111
    10010
    '''
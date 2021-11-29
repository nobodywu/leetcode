from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        if 0 == n:
            return

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 注意是顺时针旋转90度
                # n为奇数时，j比i多1
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
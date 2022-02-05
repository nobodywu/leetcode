from typing import List
import bisect


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        '''
        遍历法求解
        '''
        if not matrix or 0 == len(matrix):
            return

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if target == matrix[i][j]:
                    return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        二分法，使用python内置的bisect
        '''
        if not matrix or 0 == len(matrix):
            return

        col = len(matrix[0])

        for each in matrix:
            idx = bisect.bisect_left(each, target)
            if idx < col and each[idx] == target:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    m = [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    print(s.searchMatrix(m, 20))
    print(s.searchMatrix(m, 16))

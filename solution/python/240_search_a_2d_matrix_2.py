from typing import List


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


if __name__ == "__main__":
    s = Solution()
    m = [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    print(s.searchMatrix1(m, 20))
    print(s.searchMatrix1(m, 16))

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(c, flags, adjacency):
            '''
            flags:
            -1: 与课程相连的全部遍历过了，没有遇到1，是安全的
            0: 还未进入dfs
            1: 说明存在环
            '''
            if flags[c] == -1:
                return True

            if flags[c] == 1:
                return False

            flags[c] = 1
            for linked_crs in adjacency[c]:
                if not dfs(linked_crs, flags, adjacency):
                    return False

            # 走到这里说明不存在环，将当前课程标记为-1，是安全的
            flags[c] = -1
            return True

        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        '''
          0      1     2    3    4    5     学完上边的课程才能学下边的课程
        [[3], [3, 4], [4], [5], [5], []]
        '''
        for crs, pre in prerequisites:
            adjacency[pre].append(crs)

        for crs in range(numCourses):
            if not dfs(crs, flags, adjacency):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    # prerequisites中[a, b]表示修a前需要先修b
    print(s.canFinish(numCourses=6,
                      prerequisites=[[5, 3], [5, 4], [3, 0], [3, 1], [4, 1], [4, 2]]))

    '''
    下标   0     1      2     3    4    5    先学的课程
        [[3], [3, 4], [4],  [5], [5], [3]]   这里多加了一个，先学5才能学3，这回肯定就有问题了
    '''
    print(s.canFinish(numCourses=6,
                      prerequisites=[[5, 3], [5, 4], [3, 0], [3, 1], [4, 1], [4, 2], [3, 5]]))

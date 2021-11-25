from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)

        if 0 == size:
            return

        path = []
        ans = []
        self.dfs(path, ans, candidates, 0, size, target)

        return ans

    def dfs(self, path: list, ans: list, candidates, index, size, target):
        if 0 == target:
            ans.append(path)
            return

        if target < 0:
            return

        for i in range(index, size):
            # index = i避免产生重复
            self.dfs(path + [candidates[i]], ans, candidates, i, size, target - candidates[i])



if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
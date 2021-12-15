class Solution:
    def numTrees(self, n: int) -> int:
        '''
        动态规划
        g[n] = g[0] * g[n - 1] + g[1] * g[n - 2] + ... + g[n - 2] * g [1] + g[n - 1] * g[0]

        n = 3
        g[2] = g[0] * g[1] + g[1] * g[0] 
        g[3] = g[0] * g[2] + g[1] * g[1] + g[2] * g[0] 
        '''
        g = [0] * (n + 1)
        g[0] = 1
        g[1] = 1

        for i in range(2, n + 1):
            # left 从0到i - 1
            # right 从i - 1到0
            left = [ii for ii in range(i)]
            right = [jj for jj in range(i - 1, -1, -1)]
            # print(i, j)
            for ii in range(len(left)):
                g[i] += g[left[ii]] * g[right[ii]]

        return g[n]



if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(4))
from typing import List


class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        '''
        遍历，超时
        '''
        length = len(temperatures)
        ans = [0] * length

        for i in range(length):
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break

        return ans

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        '''
        栈，一次遍历
        '''
        length = len(temperatures)
        ans = [0] * length
        # 栈内元素为[索引, 温度]
        # 栈底到栈顶温度依次降低
        stack = []
        for i, v in enumerate(temperatures):
            while len(stack) != 0 and v > stack[-1][1]:
                # 如果当前温度大于栈顶元素，那么栈顶经过i - stack[-1][0]天后升温
                # 依次循环，直到当前温度不再大于栈顶元素
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            # 将当前温度入栈
            stack.append([i, v])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))

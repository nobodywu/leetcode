class Solution:
    def decodeString(self, s: str) -> str:
        '''
        辅助栈法
        https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
        '''
        stack, ans, s_multi = [], "", ""

        for each in s:
            if each == "[":
                # 左括号入stack，并将res和multi初始化
                stack.append((ans, s_multi))
                ans = ""
                s_multi = ""
            elif each == "]":
                # 右括号出栈
                s_ahead, s_num = stack.pop()
                ans = s_ahead + int(s_num) * ans
            elif each in "0123456789":
                # if "0" <= each <= "9":
                # 数字的情况
                s_multi += each
            else:
                # 字母的情况
                ans += each

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a2[c]]"))

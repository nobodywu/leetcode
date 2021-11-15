class Solution:
    def __init__(self) -> None:
        # 用右括号为key
        self.brackets_dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

    def isValid(self, s: str) -> bool:
        # 如果字符长度为奇数，返回False
        if len(s) % 2 != 0:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in self.brackets_dict.keys():
                # 右括号

                # 存在左括号
                if len(stack) == 0:
                    return False
                
                # 最后一个左括号与右括号对应
                if stack[-1] != self.brackets_dict[s[i]]:
                    return False

                stack.pop()

            else:
                # 左括号
                stack.append(s[i])

        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        return not stack

if __name__=="__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("({[]})"))

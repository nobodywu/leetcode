class Solution:
    def __init__(self):
        self.ans = []
        self.count = 0
        self.msg = ""

    def generateParenthesis(self, n: int) -> list:
        if n <= 0:
            return self.ans
        else:
            self.getParenthesis("", n, n)
            return self.ans

    def getParenthesis(self, ss, left, right):
        print("第{}次调用，left={}，right={}, ss={}".format(self.count, left, right, ss))
        self.count += 1
        if 0 == left and 0 == right:
            print("返回")
            self.ans.append(ss)
            return
        else:
            if left == right:
                # 相等时需要添加左括号
                print("左等于右，添加左括号")
                self.getParenthesis(ss+"(", left-1, right)
            else:
                # 可以添加左括号，也可以添加右括号
                # 添加右括号的情况不受添加左括号的情况影响
                if left > 0:
                    print("添加左括号")
                    self.getParenthesis(ss+"(", left-1, right)
                print("添加右括号")
                self.getParenthesis(ss+")", left, right-1) 

if __name__=="__main__":
    s = Solution()
    print(s.generateParenthesis(2))
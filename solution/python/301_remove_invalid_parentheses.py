from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return

        # 统计需要删除的左括号和右括号数量
        # l_nd 需要删除的左括号数量
        # r_nd 需要删除的右括号数量
        l_nd, r_nd = 0, 0
        for c in s:
            if c == "(":
                # 如果是左括号
                l_nd += 1
            elif c == ")":
                # 如果是右括号
                if l_nd == 0:
                    r_nd += 1
                else:
                    l_nd -= 1
            else:
                # 如果是其他字符不做处理
                pass

        # 计算可以保留的左括号和右括号数量
        # l_r 可以保留的左括号数量
        # r_r 可以保留的右括号数量

        l_r = s.count("(") - l_nd
        r_r = s.count(")") - r_nd
        ans = set()  # 为了去重

        # 递归函数
        # i 当前下标
        # l_dd 已经删除的左括号数量
        # r_dd 已经删除的右括号数量
        # l_u 已经使用的左括号数量
        # r_u 已经使用的右括号数量
        # f 用二进制的方法表示第几位需要被删除，从右开始，二进制右1代表下标0
        def dfs(i, l_dd, r_dd, l_u, r_u, f):
            if i == len(s):
                # 超出字符长度，结束递归
                # & 结果为0表示当前位不需要被删除
                ans.add("".join([s[_] for _ in range(len(s)) if f & 1 << _ == 0]))
                return

            if s[i] == "(":
                # 如果是左括号
                if l_dd < l_nd:
                    # 可以删除这个左括号
                    # 1左移i位表示了当前为可以被删除，与f进行|操作，保留了之前的信息
                    dfs(i + 1, l_dd + 1, r_dd, l_u, r_u, f | 1 << i)
                if l_u < l_r:
                    # 也可以保留这个左括号
                    dfs(i + 1, l_dd, r_dd, l_u + 1, r_u, f)
            elif s[i] == ")":
                if r_dd < r_nd:
                    dfs(i + 1, l_dd, r_dd + 1, l_u, r_u, f | 1 << i)
                if r_u < r_r and r_u < l_u:
                    # 已使用右括号数量小于能够使用的数量，且小于左括号已使用的数量，才能够保留右括号
                    dfs(i + 1, l_dd, r_dd, l_u, r_u + 1, f)
            else:
                # 其他字符不做任何处理，继续进入下一个字符
                dfs(i + 1, l_dd, r_dd, l_u, r_u, f)

        dfs(0, 0, 0, 0, 0, 0)

        return list(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.removeInvalidParentheses("()(()a)())"))

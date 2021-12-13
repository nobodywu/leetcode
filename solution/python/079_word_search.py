from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        visited = set()

        def check(i, j ,k):
            if board[i][j] != word[k]:
                print("board[{}, {}], 与word[{}]不一致".format(i, j, k))
                return False

            # 以下为当前board[i, j]是work[k]
            if k == len(word) - 1:
                # 到达word最后一个字符
                return True

            print("board[{}, {}], 与word[{}]一致".format(i, j, k))
            # 不是word最后一个字符
            result = False
            # 当前board[i ,j]已经访问过，向周围遍历的时候就不能再查找这个位置
            # board[i, j]的周围是否存在下一个word[k + 1]
            visited.add((i, j))
            # for pi in movement:
            #    ii = i + pi[0]
            #    jj = j + pj[1]
            for pi, pj in movement:
                print("检查word[{}]周围元素{},{}".format(k, pi, pj))
                ii = i + pi
                jj = j + pj
                if 0 <= ii and ii < m and 0 <= jj and jj < n:
                    if (ii, jj) not in visited:
                        if check(ii, jj, k + 1):
                            print("word[{}]周围元素{},{}与word[{}]一致".format(k, pi, pj, k + 1))
                            result = True
                            break
                        else:
                            print("word[{}]周围元素{},{}与word[{}]不一致".format(k, pi, pj, k + 1))
                    else:
                        print("已经访问过")
                else:
                    print("超出边界")

            visited.remove((i ,j))
            return result
        
        
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True

        return False

if __name__ == "__main__":
    s = Solution()
    # print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

    '''
    ABCE
    SFCS
    ADEE
    '''
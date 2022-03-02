from typing import List


class UnionFindWithoutWeight:
    '''
    数据结构：并查集
    不带权重
    https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/
    '''

    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        """
        root = x

        while self.father[root] != None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            # 这里把y的祖先作为x和y的公共祖先
            # 也可以把x的祖先作为x和y的公共祖先
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        判断两节点是否相连，即判断x和y的root是否相同
        """
        return self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点。把一个新节点添加到并查集中，那么它的父节点应该为空
        """
        if x not in self.father:
            self.father[x] = None


class UnionFindWithWeight:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]

        # 此时的base代表x到root的总放大倍数

        while x != root:
            original_father = self.father[x]
            # 离根节点越远，放大的倍数越高
            self.value[x] *= base
            # 减小original_father到root的放大倍数
            base /= self.value[original_father]
            #####
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点，val为x和y之间的权重
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 这里把y的祖先作为x和y的公共祖先，因此要更新x的祖先到y祖先的权重
            # x到y祖先的距离 = x到x祖先的距离 * x祖先到y祖先的距离
            # x到y的距离 = val = x到y祖先的距离 / y到y祖先的距离
            # 因此，x祖先到y祖先的距离 = y到y祖先的距离 * val / x到x祖先的距离
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        两节点是否相连。x和y都有权重，并且右相同的祖先
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点，初始化权重为1.0
        """
        if x not in self.father:
            self.father[x] = None
            # 初始化节点的权重倍数
            self.value[x] = 1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFindWithWeight()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        res = [-1.0] * len(queries)

        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]
        return res

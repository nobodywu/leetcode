# 本题是一个带权的并查集问题，定义UnionFindWithWeight类，本题的权重指倍率
# UnionFindWithWeight类包含find, add, merge, is_connected方法
# find方法：查找节点x的祖先，压缩路径并更新权重

class UnionFindWithWeight:
    def __init__(self):
        self.father = {}
        self.weight = {}

    def find(self, x):
        root = x
        rate = 1  # x到祖先的倍率

        # 查找x的祖先root，记录x的father到祖先的rate，x到father的权重可以由self.father[x]获得
        while self.father[root] != None:
            root = self.father[root]
            rate = self.weight[root] * rate

        # 压缩路径，并更新权重
        while x != root:
            cur_father = self.father[x]
            self.father[x] = root  # 直接将x的father置为root
            self.weight[x] = self.weight[x] * rate  # 更新x到father的权重
            rate = rate / self.weight[cur_father]  # 更新rate值，rate记录当前节点father到祖先的权重
            x = cur_father  # 将当前节点变为x之前的father

        return root

    def add(self, x):
        # 如果节点不存在，那么添加一个节点，
        # 添加节点即为初始化一个节点，节点的father为None，节点到father的权重（倍率）为1

        if x not in self.father:
            self.father[x] = None
            self.weight[x] = 1

    def merge(self, x, y, val):
        # x到y的权重为val
        # 需要先检查x和y是否已经连通
        root_x = self.find(x)  # 已经压缩了路径，self.weight[x]表示x到root_x的权重
        root_y = self.find(y)  # 同上

        # 如果x和y的祖先不一样
        if root_x != root_y:
            # 把两个祖先相连，将root_x的father设置为root_y
            self.father[root_x] = root_y
            # 设置root_x到root_y的距离，根据四边形法则
            self.weight[root_x] = self.weight[y] * val / self.weight[x]

    def is_connected(self, x, y):
        # x in self.weight 即为 x in self.weight.keys()
        return x in self.weight and y in self.weight and self.find(x) == self.find(y)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ufww = UnionFindWithWeight()

        # 根据equations和values构建带权的并查集
        # zip函数，把对应的元素组成一个tuple
        for (x, y), val in zip(equations, values):
            ufww.add(x)
            ufww.add(y)
            ufww.merge(x, y, val)

        # ans = [-1.0] * len(queries)
        ans = [-1.0 for _ in range(len(queries))]
        for i, (a, b) in enumerate(queries):
            if ufww.is_connected(a, b):
                # a和b有共同的祖先，那么a到b的权重（倍率）为ufww.weight[a] / ufww.weight[b]
                ans[i] = ufww.weight[a] / ufww.weight[b]

        return ans

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    '''
    https://blog.csdn.net/acarsar/article/details/87899717
    '''

    def __init__(self) -> None:
        self.root = None
        self.a = []  # 用来存放左右子节点未满的根节点

    def add(self, number: int):
        '''
        number中的None或"null"统一替换为"null"，用来表示当前节点为空
        判断逻辑中None表示节点还未被赋值
        最后再把"null"统一替换为None
        '''
        # print("add: ", number)
        if number == None or number == "null":
            node = "null"
        else:
            node = TreeNode(number)

        if self.root == None:
            self.root = node
            self.a.append(self.root)
        else:
            if self.a[0].left == None:
                # print("为{}添加左节点{}".format(self.a[0].val, number))
                self.a[0].left = node
                if node != "null":
                    self.a.append(node)  # 新增加的左节点没有左右子节点
            elif self.a[0].right == None:
                # print("为{}添加右节点{}".format(self.a[0].val, number))
                self.a[0].right = node
                if node != "null":
                    self.a.append(node)  # 新增加的右节点没有左右子节点

                if "null" == self.a[0].left:
                    self.a[0].left = None

                if "null" == self.a[0].right:
                    self.a[0].right = None

                self.a.pop(0)  # 当前节点左右子节点已满，要去除
        # print(self.a)

    def serialize(self, root):
        """
        将二叉树序列化，leetcode上要求结果是字符串
        From 297
        """
        if not root:
            return ""
        q = deque()
        q.append(root)
        res = str()
        while q:
            node = q.popleft()
            if node != None:
                res += (str(node.val) + ".")
                q.append(node.left)
                q.append(node.right)
            else:
                res += "None."

        while res[-1] == None:
            res.pop()

        return res

    def deserialize(self, data):
        """
        将字符串变为二叉树
        From 297
        """
        if not data:
            return None

        data = data.split(".")
        root = TreeNode(data.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            if data:
                val = data.pop(0)
                if val != "None":
                    node.left = TreeNode(val)
                    q.append(node.left)
            if data:
                val = data.pop(0)
                if val != "None":
                    node.right = TreeNode(val)
                    q.append(node.right)
        return root


if __name__ == "__main__":
    t = Tree()  # 二叉树类的实例化
    L = [1, 2, 3, 4, None, 5, 6, 7, 8, 9]
    for i in L:
        t.add(i)
        # print('节点添加成功')

    print(t.root.right.left.left.val)

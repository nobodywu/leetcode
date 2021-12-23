# Definition for a binary tree node.
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
        self.a = [] # 用来存放左右子节点未满的根节点

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
                    self.a.append(node) # 新增加的左节点没有左右子节点
            elif self.a[0].right == None:
                # print("为{}添加右节点{}".format(self.a[0].val, number))
                self.a[0].right = node
                if node != "null":
                    self.a.append(node) # 新增加的右节点没有左右子节点

                if "null" == self.a[0].left:
                    self.a[0].left = None

                if "null" == self.a[0].right:
                    self.a[0].right = None

                self.a.pop(0) # 当前节点左右子节点已满，要去除
        # print(self.a)


if __name__=="__main__":
    t = Tree()  # 二叉树类的实例化
    L = [1, 2, 3, 4, None, 5, 6, 7, 8, 9]
    for i in L:
        t.add(i)
        # print('节点添加成功')

    print(t.root.right.left.left.val)
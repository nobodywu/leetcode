# Definition for a binary tree node.
from collections import deque
from type import binary_tree_node


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS 广度优先
class Codec:
    def serialize(self, root):
        """
        将二叉树序列化，leetcode上要求结果是字符串
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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    t = binary_tree_node.Tree()  # 二叉树类的实例化
    # l = [1, "null", 2, 3]
    l = [1, 2, 3, None, None, 4, 5]  # python中没有null
    for i in l:
        t.add(i)
        # print('节点添加成功')
    # print(t.root.left.left.right)
    s = Codec()
    print(s.serialize(t.root))
    r = s.deserialize(s.serialize(t.root))
    print(s.serialize(r))

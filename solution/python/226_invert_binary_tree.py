from re import S
from type import binary_tree_node

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root


if __name__ == "__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [4, 2, 7, 1, 3, 6, 9]
    for i in l:
        t.add(i)
        print('节点添加成功')

    s.invertTree(t.root)

    print(t.root.val)
    print(t.root.left.val)
    print(t.root.right.val)

    '''
    需要补充二叉树逐行打印（层序遍历）
    https://blog.csdn.net/qq_20011607/article/details/89142173
    '''

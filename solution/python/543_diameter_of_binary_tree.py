from type import binary_tree_node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dsf(node: TreeNode):
            if not node:
                return 0

            l_count = dsf(node.left)  # 左支不包含当前node的最大节点数
            r_count = dsf(node.right)  # 右支不包含当前node的最大节点数
            cur_max = l_count + r_count + 1  # 以当前节点为根节点的路径上的最大节点数
            self.ans = max(self.ans, cur_max)
            # 如果当前节点为父节点的左子节点
            # 则返回值为父节点左支上的最大节点数
            # +1 即为加上当前节点
            return max(l_count, r_count) + 1

        self.ans = 1  # 最大路径上的节点数
        dsf(root)
        return self.ans - 1  # 最大路径数为节点数 - 1


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    t = binary_tree_node.Tree()

    for each in l:
        t.add(each)

    s = Solution()
    print(s.diameterOfBinaryTree(t.root))

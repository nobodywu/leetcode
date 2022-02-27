from operator import le
from type import binary_tree_node

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:

        # 抢劫当前节点node时获得的最大收益
        def rob_in(node):
            result = [0, 0]  # 第一个元素表示不抢当前节点，第二个元素表示抢当前节点

            if not node:
                return result

            left = rob_in(node.left)
            right = rob_in(node.right)

            # 如果不抢当前节点，那么最大收益为左孩子的最大收益 + 右孩子的最大收益
            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            # 如果抢当前节点，那么最大收益为不抢左孩子的最大收益 + 不抢右孩子的最大收益 + 当前节点收益
            result[1] = left[0] + right[0] + node.val

            return result

        result = rob_in(root)
        return max(result)


if __name__ == "__main__":
    t = binary_tree_node.Tree()

    l = [3, 2, 3, None, 3, None, 1]

    for each in l:
        t.add(each)

    s = Solution()

    print(s.rob(t.root))

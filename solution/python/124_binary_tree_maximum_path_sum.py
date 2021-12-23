# Optional[X] is equivalent to Union[X, None].
'''
python定义集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y) 
'''
from typing import Optional
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.sum_gain = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(node: TreeNode):
            if node == None:
                return 0

            # print("======", node.val)
            # 获得左子节点的最大路径
            left_gain = max(maxGain(node.left), 0)
            # 获得右子节点的最大路径
            right_gain = max(maxGain(node.right), 0)

            # print(self.sum_gain, node.val + left_gain + right_gain)
            self.sum_gain = max(self.sum_gain, node.val + left_gain + right_gain) # 更新最大路径值
            # print("******节点:{}的左子节点最大路径为{}，右子节点最大路径为{}, sum_gain为{}".format(node.val, left_gain, right_gain, self.sum_gain))

            return node.val + max(left_gain, right_gain) # 返回当前节点最大的路径

        maxGain(root)

        return self.sum_gain

if __name__ == "__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [-10,9,20,None,None,15,7]
    for i in l:
        t.add(i)
        print('节点添加成功')

    # print(t.root.left.right.val)
    print(s.maxPathSum(t.root))

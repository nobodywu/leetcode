from typing import Optional
from type import binary_tree_node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 采用逆中序遍历然后累加

        def dsf(node):
            if node:
                dsf(node.right)
                self.total += node.val
                node.val = self.total
                dsf(node.left)

        self.total = 0
        dsf(root)
        return root


if __name__ == "__main__":
    '''
    二叉搜索树是一棵空树，或者是具有下列性质的二叉树：
    - 若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    - 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    - 它的左、右子树也分别为二叉搜索树；
    - 二叉搜索树的中序遍历是一个单调递增的有序数列。

    本题中要求我们将每个节点的值修改为原来的节点值加上所有大于它的节点值之和。
    '''
    l = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    t = binary_tree_node.Tree()

    for each in l:
        t.add(each)

    s = Solution()
    print(t.serialize(s.convertBST(t.root)))

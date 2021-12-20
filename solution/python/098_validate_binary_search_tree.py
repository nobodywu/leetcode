from typing import List
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。
        左子节点小于上边的所有根节点
        右子节点大于上边的所有根节点
        '''

        def isValidChild(node, min = float("-inf"), max = float("inf")):
            if None == node:
                return True

            val = node.val

            # 在自己定义的二叉树中，如果节点为空，python没有null类型，则值为字符“null”。也可以使用None表示空节点
            if "null" == val:
                return True

            if val <= min or val >= max:
                return False

            # update min to check left child
            if not isValidChild(node.left, min, val):
                return False

            # update max to check right child
            if not isValidChild(node.right, val, max):
                return False

            return True

        return isValidChild(root)

if __name__ == "__main__":
    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [2, 1, 3]
    for i in l:
        t.add(i)
        print('节点添加成功')
    s = Solution()
    print(s.isValidBST(t.root))

    t2 = binary_tree_node.Tree()
    l2 = [5, 4, 6,"null", "null", 3, 7]
    for i in l2:
        t2.add(i)
        print('节点添加成功')

    s = Solution()
    print(s.isValidBST(t2.root))
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_list = []
        def preorderTraversal(root):
            if not root:
                return

            preorder_list.append(root)
            preorderTraversal(root.left)
            preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorder_list)

        for i in range(1, size):
            # id(prev) == id(preorder_list[i - 1])
            prev, curr = preorder_list[i - 1], preorder_list[i]
            # print(id(prev), id(preorder_list[i - 1]), id(curr), id(preorder_list[i]))
            prev.left = None
            prev.right = curr

if __name__=="__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [1,2,5,3,4,None,6]
    for i in l:
        t.add(i)
        print('节点添加成功')

    s.flatten(t.root)
    print(t.root.val)
    print(t.root.right.val)
    print(t.root.right.right.val)
from typing import List
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        中序遍历首先遍历左子树，然后访问根结点，最后遍历右子树。
        '''
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root: binary_tree_node.TreeNode, ans: list):
        if not root:
            return
        
        self.inorder(root.left, ans)

        # if root.val != "null":
        if root.val: # l = [1, None, 2, 3]
            ans.append(root.val)

        self.inorder(root.right, ans)

if __name__ == "__main__":
    t = binary_tree_node.Tree()  # 二叉树类的实例化
    # l = [1, "null", 2, 3]
    l = [1, None, 2, 3] # python中没有null
    for i in l:
        t.add(i)
        # print('节点添加成功')
    # print(t.root.left.left.right)
    s = Solution()
    print(s.inorderTraversal(t.root))
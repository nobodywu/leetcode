from typing import List
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        前序遍历（根左右）: 访问根结点，再访问左子树、再访问右子树。
        中序遍历（左根右）: 先访问左子树，再访问根结点、再访问右子树。
        后续遍历（左右根）: 先访问左子树，再访问右子树，再访问根结点。
        层序遍历
        '''
        def findChild(inorder: list):
            ele = preorder.pop(0) # 前序遍历的第一个元素为根节点
            node = TreeNode(ele)
            ele_idx = inorder.index(ele)
            left_sub_tree = inorder[:ele_idx] # 中序遍历中的左子树
            right_sub_tree = inorder[ele_idx + 1:] # 中序遍历中的右子树
            
            if left_sub_tree:
                node.left = findChild(left_sub_tree) # 在中序遍历的左子树中查找当前节点的左子节点。对中序遍历不断分割，直到最后一个节点
            else:
                node.left = None

            if right_sub_tree:
                node.right = findChild(right_sub_tree) # 在中序遍历的右子树中查找当前节点的右子节点。对中序遍历不断分割，直到最后一个节点
            else:
                node.right = None

            return node

        if not preorder or not inorder:
            return None

        return findChild(inorder)

if __name__ == "__main__":
    '''
            3
          /   \
        9      20
             /    \
           15      7
    '''
    s = Solution()
    print(s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))

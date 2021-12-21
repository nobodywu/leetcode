from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        深度优先搜索
        '''
        if None == root:
            return 0

        max_depths = max(self.maxDepth(root.left), self.maxDepth(root.right))

        return max_depths + 1

if __name__ == "__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [3,9,20,None,None,15,7]
    for i in l:
        t.add(i)
        print('节点添加成功')

    print(s.maxDepth(t.root))
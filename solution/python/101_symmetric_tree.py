from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        '''
        递归
        '''

        def check(node1: TreeNode, node2: TreeNode):
            if None == node1 and None == node2:
                return True

            # 此时不会同时为None
            if None == node1 or None == node2:
                return False

            return node1.val == node2.val and check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)

    def isSymmetric2(self, root: TreeNode) -> bool:
        '''
        迭代
        '''
        temp = [] # 用来存放未检查过的节点
        temp.append(root)
        temp.append(root)

        while len(temp) >= 2:
            node1 = temp[0]
            node2 = temp[1]

            temp = temp[2:]

            if None == node1 and None == node2:
                # 继续检查未检查的node
                continue

            # 此时不会同时为None
            if None == node1 or None == node2:
                return False

            if node1.val != node2.val:
                return False

            temp.append(node1.left)
            temp.append(node2.right)

            temp.append(node1.right)
            temp.append(node2.left)

        return True

if __name__ == "__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [1,2,2,3,4,4,3]
    for i in l:
        t.add(i)
        print('节点添加成功')

    print(s.isSymmetric2(t.root))

    t2 = binary_tree_node.Tree()  # 二叉树类的实例化
    l2 = [1,2,2,None,3,None,3]
    for i in l2:
        t2.add(i)
        print('节点添加成功')

    print(s.isSymmetric2(t2.root))
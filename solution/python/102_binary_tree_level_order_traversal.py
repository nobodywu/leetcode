from typing import List
from type import binary_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        广度优先搜索
        '''
        ans = []

        if None == root:
            return ans

        temp1 = []
        temp1.append(root)

        i = 0
        while len(temp1) > 0:
            # print(len(temp1))
            ans.append([]) # 在列表中添加一个子列表，用来存放该层所有node的值
            temp2 = [] # 用来存放该层所有node的子节点
            size = len(temp1) # 遍历该层所有node

            # temp1 是每一层的节点
            # temp2 是每一层的子节点
            for j in range(size):
                node = temp1[j]
                if node.val != None:
                    ans[i].append(node.val) # 把所有temp1中的node值放入ans[i]

                if node.left != None:
                    temp2.append(node.left)

                if node.right != None:
                    temp2.append(node.right)

            temp1 = temp2
            i += 1
            # print(ans)

        return ans



if __name__ == "__main__":
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [3,9,20,None,None,15,7]
    for i in l:
        t.add(i)
        print('节点添加成功')

    print(s.levelOrder(t.root))
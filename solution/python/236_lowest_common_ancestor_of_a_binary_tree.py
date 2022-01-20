from pytest import LogCaptureFixture
from type import binary_tree_node

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归边界，子树没有p或q
        if None == root:
            print("root is None, return None")
            return None

        print("current root is {}".format(root.val))

        # 递归边界，子树有p或q
        if root.val == p.val or root.val == q.val:
            print("root {} is equal to p {} or q {}, return root {}".format(root.val, p.val, q.val, root.val))
            return root

        # 采用后续遍历的方式进行
        print("call lowestCommonAncestor, left")
        left = self.lowestCommonAncestor(root.left, p, q)
        print("call lowestCommonAncestor, right")
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右都不为None，那么root就是最近公共祖先。如果是parent的left，那么parent的right全为None，最终return 这个left层层往上返回。反之类似
        if left != None and right != None:
            print("left != None and right != None, return root ", root.val)
            return root

        # p和q同在左子树，或同在右子树中
        # return left if left != None else right

        # 如果pq全部在左子树，那么最终返回上边的left（看p或q哪个在上边），这个left层层往上返回
        if left:
            print("left is not None and right is None, return left ", left)
            return left

        # 同上
        if right:
            print("left is None and right is not None, return right ", right)
            return right

        print("left and right are None, return None")
        return None


if __name__ == "__main__":
    '''
              1
        2           3
     4     5     6     7
    8 9  10 11 12 13 14 15
    '''
    s = Solution()

    t = binary_tree_node.Tree()  # 二叉树类的实例化
    l = [i for i in range(1, 16)]
    print(l)
    for i in l:
        t.add(i)
        print('节点添加成功')

    ancestor = s.lowestCommonAncestor(t.root, t.root.left.left.right, t.root.left.right.right)
    print(ancestor.val)

    '''
    current root is 1
    call lowestCommonAncestor, left。根据返回结果，1的左子树包含p(9)和q(11)
        current root is 2
        call lowestCommonAncestor, left。根据返回结果，2的左子树包含p(9)
            current root is 4
            call lowestCommonAncestor, left。根据返回结果，4的左子树不包含pq
                current root is 8
                call lowestCommonAncestor, left
                    root is None, return None
                call lowestCommonAncestor, right
                    root is None, return None
                left and right are None, return None
            call lowestCommonAncestor, right。根据返回结果，4的右子树包含p(9)
                current root is 9
                root 9 is equal to p 9 or q 11, return root 9
            left is None and right is not None, return right  <type.binary_tree_node.TreeNode object at 0x7f818aec0370>
        call lowestCommonAncestor, right。根据返回结果，2的右子树包含q(11)
            current root is 5
            call lowestCommonAncestor, left。根据返回结果，5的左子树不包含pq
                current root is 10
                    call lowestCommonAncestor, left
                        root is None, return None
                    call lowestCommonAncestor, right
                        root is None, return None
                left and right are None, return None
            call lowestCommonAncestor, right。根据返回结果，5的右子树包含q(11)
                current root is 11
                root 11 is equal to p 9 or q 11, return root 11
            left is None and right is not None, return right  <type.binary_tree_node.TreeNode object at 0x7f818aec0430>
        left != None and right != None, return root  2

    call lowestCommonAncestor, right
        current root is 3
        call lowestCommonAncestor, left
            current root is 6
            call lowestCommonAncestor, left
                current root is 12
                call lowestCommonAncestor, left
                    root is None, return None
                call lowestCommonAncestor, right
                    root is None, return None
                left and right are None, return None
            call lowestCommonAncestor, right
                current root is 13
                call lowestCommonAncestor, left
                    root is None, return None
                call lowestCommonAncestor, right
                    root is None, return None
                left and right are None, return None
            left and right are None, return None
        call lowestCommonAncestor, right
            current root is 7
            call lowestCommonAncestor, left
                current root is 14
                call lowestCommonAncestor, left
                    root is None, return None
                call lowestCommonAncestor, right
                    root is None, return None
                left and right are None, return None
            call lowestCommonAncestor, right
                current root is 15
                call lowestCommonAncestor, left
                    root is None, return None
                call lowestCommonAncestor, right
                    root is None, return None
                left and right are None, return None
            left and right are None, return None
        left and right are None, return None

    left is not None and right is None, return left  <type.binary_tree_node.TreeNode object at 0x7f818af038b0>。此时返回节点2
    lowest common ancestor is 2
    '''

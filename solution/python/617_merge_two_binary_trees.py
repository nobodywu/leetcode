from type.binary_tree_node import Tree, TreeNode


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2

        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged


if __name__ == "__main__":
    l1 = [1, 3, 2, 5]
    l2 = [2, 1, 3, None, 4, None, 7]

    t1 = Tree()
    t2 = Tree()
    for each in l1:
        t1.add(each)

    for each in l2:
        t2.add(each)

    s = Solution()
    print(t1.serialize(s.mergeTrees(t1.root, t2.root)))

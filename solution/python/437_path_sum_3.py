from type import binary_tree_node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def dfs(node, target, path_sum_count_dict, pre_sum):
            # count表示当前层路径和为target的计数
            count = 0

            if not node:
                return count

            # 计算前缀和
            pre_sum += node.val

            if pre_sum - target in path_sum_count_dict:
                # 从root到节点A的路径和为presum1，
                # 从root到节点B的路径和为presum2，
                # 如果presum2 - presum1 = target
                # 那么从节点A到节点B的路径和为target
                # 那么路径和为target的计数既为
                # 字典中路径和为presmum2 - target的计数
                count += path_sum_count_dict[pre_sum - target]

            # 准备进入下一层，更新当前路径和的计数
            if pre_sum not in path_sum_count_dict:
                path_sum_count_dict[pre_sum] = 1
            else:
                path_sum_count_dict[pre_sum] += 1

            # 进入下一层
            count += dfs(node.left, target, path_sum_count_dict, pre_sum)
            count += dfs(node.right, target, path_sum_count_dict, pre_sum)

            # 回溯时要对路径和的计数进行还原
            path_sum_count_dict[pre_sum] -= 1

            return count

        # key表示路径和的值，value表示前缀和为key的路径个数
        path_sum_count_dict = {0: 1}
        count = dfs(root, targetSum, path_sum_count_dict, 0)
        return count


if __name__ == "__main__":
    t = binary_tree_node.Tree()
    l = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    for each in l:
        t.add(each)

    s = Solution()
    print(s.pathSum(t.root, 8))

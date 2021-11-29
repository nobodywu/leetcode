from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)

        if 0 == size:
            return

        ans = []

        def backtrace(first = 0):

            if first == size:
                # https://blog.csdn.net/qq_24502469/article/details/104185122
                # https://www.cnblogs.com/doublexi/p/8745792.html dict的key是第一层，value是第二层
                # ans.append(nums)是非拷贝，这里只记录了nums的地址，而内容会还原回去
                # list.copy() == list[:]，为浅拷贝，只对第一层深拷贝，可以使用，因为nums仅一层
                ans.append(copy.deepcopy(nums))
                print("添加nums, {}. ans, {}".format(nums, ans))

            # 如果 first == size，在for内无操作
            for i in range(first, size):
                nums[first], nums[i] = nums[i], nums[first]
                print("交换{}和{},nums为{}".format(first, i, nums))
                backtrace(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
                print("还原{}和{},nums为{}".format(first, i, nums))

        backtrace()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))
from typing import List

class Solution:
    def trap1(self, height: List[int]) -> int:
        '''
        按列求，超出时间限制
        '''

        if not height:
            return
        
        size = len(height)
        ans = 0
        for i in range(size):
            left_max, right_max = 0, 0

            for l in range(i):
                if height[l] > left_max:
                    left_max = height[l]

            for r in range(i, size):
                if height[r] > right_max:
                    right_max = height[r]

            if min(left_max, right_max) > height[i]:
                ans += min(left_max, right_max) - height[i]

        return ans

    def trap2(self, height: List[int]) -> int:
        '''
        双指针
        '''
        if not height:
            return

        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                # 更新left_max
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]

                left += 1

            else:
                # 更新right_max
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]

                right -= 1

        return ans



if __name__ == "__main__":
    s = Solution()
    print(s.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
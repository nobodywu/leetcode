class Solution:
    '''
    双指针 + 哈希。以索引为思路，本质上和滑动窗口思想一致。
    '''

    def lengthOfLongestSubstring1(self, s: str) -> int:
        # 定义左右两个索引index_l, index_r并初始化为0
        # 进入下边循环，直到index_r到达字符串的末尾
        #     - 将当前index_r表示的字符放入sub_str_dict中。统计当前[index_l, index_r]间的字符数量
        #     - 如果index_r所代表的字符char_r在字典中的数量是否大于1，则进入循环，直到不在大于1
        #         - 剔除字典中index_l所代表的字符
        #         - index_l向后移动
        #     - 当前子串为无重复的字串，长度为index_r - index_l + 1。更新最大无重复字符串长度
        # 时间复杂度O(N)
        # 空间复杂度O(1)

        if not s:
            return 0

        index_l = 0
        index_r = 0
        sub_str_dict = {}
        max_len = 0

        while index_r < len(s):
            char_r = s[index_r]
            sub_str_dict[char_r] = sub_str_dict[char_r] + 1 if sub_str_dict.get(char_r) else 1
            while sub_str_dict[char_r] > 1:
                char_l = s[index_l]
                sub_str_dict[char_l] -= 1
                index_l += 1

            max_len = max(max_len, index_r - index_l + 1)

            index_r += 1

        return max_len

    '''
    滑动窗口
    '''

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 初始化字符串窗口temp_str和最长子串max_str为空
        # 遍历字符串s，依次向temp_str末尾添加字符c前需要考虑c是否已经出现在temp_str
        #     - 如果c不在temp_str中。temp_str + c
        #     - 如果c在temp_str中。那么temp_str是一个无重复子串，需要判断是否为最长
        #         - temp_str是最长。max_str = temp_str，重置temp_str为temp_str[temp_str.index(c) + 1:] + c
        #         - temp_str不是最长。重置temp_str为temp_str[temp_str.index(c) + 1:] + c
        # 如果无重复字符的最长子串在s末尾，那么需要在最后进行一次判断并对max_str赋值
        # 时间复杂度O(N)
        # 空间复杂度O(1)

        temp_str = ''
        max_str = ''

        for each in list(s):

            if each not in temp_str:
                temp_str += each

            else:
                # s.index()的返回值从0开始，如果不存在抛出错误
                c_index = temp_str.index(each)
                if len(max_str) < len(temp_str):
                    max_str = temp_str
                    temp_str = temp_str[c_index + 1:] + each

                else:
                    temp_str = temp_str[c_index + 1:] + each

        # 考虑最长数组即为原始数据，和最长数组在末尾的情况
        if len(max_str) < len(temp_str):
            max_str = temp_str

        return len(max_str)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring1("pwwkew"))  # should be 3
    print(s.lengthOfLongestSubstring1(" "))  # should be 1
    print(s.lengthOfLongestSubstring1("aab"))  # should be 2
    print(s.lengthOfLongestSubstring1("dvdf"))  # should be 3
    print(s.lengthOfLongestSubstring1("aabaab!bb"))  # should be 3

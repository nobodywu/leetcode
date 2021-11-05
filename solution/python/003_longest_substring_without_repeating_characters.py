class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp_str = ''
        max_str = ''

        for each in list(s):
 
            if each not in temp_str:
                temp_str += each

            else:
                c_index = temp_str.index(each)
                if len(max_str) < len(temp_str):
                    max_str = temp_str
                    temp_str = temp_str[c_index + 1:] + each

                else:
                    temp_str = temp_str[c_index + 1:] + each

        if max_str:
            if len(max_str) > len(temp_str):
                return len(max_str)
            else:
                return len(temp_str)
        else:
            return len(temp_str)

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew")) # should be 3
    print(s.lengthOfLongestSubstring(" ")) # should be 1
    print(s.lengthOfLongestSubstring("aab")) # should be 2
    print(s.lengthOfLongestSubstring("dvdf")) # should be 3
    print(s.lengthOfLongestSubstring("aabaab!bb")) # should be 3
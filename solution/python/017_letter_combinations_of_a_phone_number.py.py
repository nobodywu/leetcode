class Solution:
    def __init__(self) -> None:
        self.digits_map = {}
        self.digits_map['2'] = "abc"
        self.digits_map['3'] = "def"
        self.digits_map['4'] = "ghi"
        self.digits_map['5'] = "jkl"
        self.digits_map['6'] = "mno"
        self.digits_map['7'] = "pqrs"
        self.digits_map['8'] = "tuv"
        self.digits_map['9'] = "wxyz"

    def letterCombinations(self, digits: str) -> list:
        if 0 == len(digits):
            return []

        combination = []
        combinations = []

        def traceLeter(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                num = digits[index]
                for letter in self.digits_map[num]:
                    combination.append(letter)
                    traceLeter(index + 1)
                    combination.pop() # 去掉最后一个

        traceLeter(0)

        return combinations

if __name__=="__main__":
    s = Solution()
    print(s.letterCombinations("24"))
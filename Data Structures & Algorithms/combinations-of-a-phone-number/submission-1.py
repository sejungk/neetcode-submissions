class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # res = [""]
        # for digit in digits:
        #     temp = []
        #     for string in res:
        #         for char in digit_to_char[digit]:
        #             temp.append(string + char)
        #     res = temp
        # return res

        res = []
        def dfs(digit_idx, combo):
            if digit_idx == len(digits):
                if combo:
                    res.append(combo)
                return

            for char in digit_to_char[digits[digit_idx]]:
                dfs(digit_idx + 1, combo + char)

        dfs(0, "")
        return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {}
        num_to_letters["2"] = "abc"
        num_to_letters["3"] = "def"
        num_to_letters["4"] = "ghi" 
        num_to_letters["5"] = "jkl"
        num_to_letters["6"] = "mno"
        num_to_letters["7"] = "pqrs"
        num_to_letters["8"] = "tuv"
        num_to_letters["9"] = "wxyz"

        res = []
        def dfs(digit_idx, combo):
            if digit_idx == len(digits):
                if combo:
                    res.append(combo)
                return

            for char in num_to_letters[digits[digit_idx]]:
                combo += char
                dfs(digit_idx + 1, combo)
                combo = combo[:-1]

        dfs(0, "")
        return res
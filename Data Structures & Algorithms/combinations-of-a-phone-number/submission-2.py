class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def dfs(i, arr):
            if i == len(digits):
                res.append("".join(arr))
                return
            
            for l in letters[digits[i]]:
                arr.append(l)
                dfs(i + 1, arr)
                arr.pop()

        dfs(0, [])
        return res
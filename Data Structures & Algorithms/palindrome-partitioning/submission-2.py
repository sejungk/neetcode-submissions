class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def create_palindromes(parts, i):
            if i == len(s):
                if parts[-1] and parts[-1] == parts[-1][::-1]:
                    res.append(parts.copy())
                return

            parts[-1] += s[i]
            if parts[-1] == parts[-1][::-1]:
                parts.append("")
                create_palindromes(parts, i + 1)
                parts.pop()
                
            create_palindromes(parts, i + 1)

        create_palindromes([""], 0)
        return res

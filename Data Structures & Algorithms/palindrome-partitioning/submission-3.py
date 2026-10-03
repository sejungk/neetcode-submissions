class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = {}
        n = len(s)
        
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes.setdefault(left, []).append(right)
                left -= 1
                right += 1

        for mid in range(n):
            expand(mid, mid)      # Odd-length palindromes
            expand(mid, mid + 1)  # Even-length palindromes
               

        res = []
        def dfs(start, substrings):
            if start == len(s):
                res.append(substrings.copy())
                return

            if start not in palindromes:
                return

            for end in palindromes[start]:
                substrings.append(s[start: end + 1])
                dfs(end + 1, substrings)
                substrings.pop()
        
        dfs(0, [])
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        def is_pali(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i-= 1
                j += 1

            return s[i + 1:j]

        pali = ""
        for i in range(1, n):
            even = is_pali(i - 1, i)
            odd = is_pali(i, i)

            if len(even) > len(pali):
                pali = even
            if len(odd) > len(pali):
                pali = odd
        
        return pali
            

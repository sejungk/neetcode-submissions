class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        res = 0
        def is_pali(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        for i in range(n):
            res += is_pali(i, i + 1)
            res += is_pali(i, i)
        
        return res

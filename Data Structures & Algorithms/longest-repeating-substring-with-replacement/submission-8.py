class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counts = defaultdict(int)
        res = 0

        l = 0
        max_freq_cnt = 0
        for r in range(n):
            counts[s[r]] += 1
            max_freq_cnt = max(max_freq_cnt, counts[s[r]])

            while (r - l + 1) - max_freq_cnt > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
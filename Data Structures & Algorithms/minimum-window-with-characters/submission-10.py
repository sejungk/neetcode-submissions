from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        start = -1
        min_len = float("inf")
        counts = defaultdict(int)

        for c in t:
            counts[c] += 1

        found = len(counts)
        l = 0
        r = 0

        while r < n:
            if s[r] in counts:
                counts[s[r]] -= 1
                if counts[s[r]] == 0:
                    found -= 1

            if found == 0:
                break

            r += 1

        if found != 0:
            return ""

        # Start shrinking from the first valid window
        while r < n:
            while l <= r and (s[l] not in counts or counts[s[l]] < 0):
                if s[l] in counts:
                    counts[s[l]] += 1
                l += 1

            if r - l + 1 < min_len:
                min_len = r - l + 1
                start = l

            r += 1

            if r < n and s[r] in counts:
                counts[s[r]] -= 1

        return s[start:start + min_len]
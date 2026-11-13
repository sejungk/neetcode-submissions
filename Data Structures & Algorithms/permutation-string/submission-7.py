
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = defaultdict(int)
        count = 0

        for char in s1:
            seen[char] += 1
            count += 1

        l = 0
        for r in range(len(s2)):
            if (r - l + 1) <= len(s1):
                if s2[r] in seen:
                    if seen[s2[r]] > 0:
                        count -= 1
                    seen[s2[r]] -= 1

            if (r - l + 1) == len(s1):
                if count == 0:
                    return True

                if s2[l] in seen:
                    if seen[s2[l]] >= 0:
                        count += 1
                    seen[s2[l]] += 1

                l += 1

        return False

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) - 1

        chars_needed = len(set(t))
        min_length = float('inf')
        min_start = 0
        left = 0
        for right in range(len(s)):
            if s[right] in t_counts:
                t_counts[s[right]] += 1
                if t_counts[s[right]] == 0:
                    chars_needed -= 1

            if chars_needed == 0:
                while left < right and (s[left] not in t_counts or t_counts[s[left]] > 0):
                    if s[left] in t_counts:
                        t_counts[s[left]] -= 1
                    left += 1
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_start = left
                
        if min_length == float('inf'):
            return ""
        else:
            return s[min_start: min_start + min_length]

        



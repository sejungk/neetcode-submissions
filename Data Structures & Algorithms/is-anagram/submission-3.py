class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for char in s:
            seen[char] += 1
        
        for char in t:
            if char not in seen:
                return False
            
            seen[char] -= 1
            if seen[char] < 0:
                return False

            if seen[char] == 0:
                del seen[char]
        
        return len(seen) == 0
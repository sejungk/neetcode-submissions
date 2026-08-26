class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}

        for char in s:
            visited[char] = visited.get(char, 0) + 1

        for char in t:
            if char not in visited:
                return False
            visited[char] -= 1

        for char in visited:
            if visited[char] != 0:
                return False
        
        return True
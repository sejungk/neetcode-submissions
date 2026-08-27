class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        key = [0]*26

        for char in s1:
            key[ord(char) - ord('a')] += 1
        
        left = 0
        curr_key = [0]*26
        for right in range(n):
            curr_key[ord(s2[right]) - ord('a')] += 1
            if (right - left + 1) != len(s1):
                continue
            
            if curr_key == key:
                return True

            curr_key[ord(s2[left]) - ord('a')] -= 1
            left += 1
            print(curr_key, key, left, right)
        
        return False
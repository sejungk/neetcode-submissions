class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        key = [0]*26

        for char in s1:
            key[ord(char) - ord('a')] += 1
        
        for left in range(n):
            left_char_key = ord(s2[left]) - ord("a")
            if (key[left_char_key]) == 0:
                continue
            
            right = left
            curr_key = [0]*26
            while right < len(s2) and right - left < len(s1):
                curr_key_idx = ord(s2[right]) - ord("a")
                if (key[curr_key_idx] < curr_key[curr_key_idx] + 1):
                    break
                curr_key[curr_key_idx] += 1
                # print(curr_key, key)
                if curr_key == key:
                    return True
                right += 1
                
        return False
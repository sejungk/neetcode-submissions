class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        matches = 0

        for char in s1:
            s1_count[ord(char) - ord("a")] += 1
        
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        if matches == 26:
            return True
        #s1 = "abc", s2 = "l e c a b e e"
        #                    l   r
        left = 0
        for right in range(len(s1), len(s2)):
            right_key_idx = ord(s2[right]) - ord("a")
            s2_count[right_key_idx] += 1
            if s2_count[right_key_idx] == s1_count[right_key_idx]:
                matches += 1
            elif s2_count[right_key_idx] - 1 == s1_count[right_key_idx]:
                matches -= 1

            left_key_idx = ord(s2[left]) - ord("a")
            s2_count[left_key_idx] -= 1
            if s2_count[left_key_idx] == s1_count[left_key_idx]:
                matches += 1
            elif s2_count[left_key_idx] + 1 == s1_count[left_key_idx]:
                matches -= 1
            left += 1
            
            if matches == 26: 
                return True
        return False

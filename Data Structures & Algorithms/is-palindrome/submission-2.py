class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and not self.alpha_num(s[left]):
                left += 1
            
            while left < right and not self.alpha_num(s[right]):
                right -= 1
        
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        
    
    def alpha_num(self, char):
        return (ord("A") <= ord(char) <= ord("Z") or 
                ord("a") <= ord(char) <= ord("z") or
                ord('0') <= ord(char) <= ord("9")) 
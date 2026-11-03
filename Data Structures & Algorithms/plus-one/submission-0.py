class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0

        digits[n-1] += 1
        for i in range(n - 1, -1, -1):
            sum = digits[i] + carry 

            if carry == 1:
                carry = 0

            if sum > 9:
                carry = 1
            
            digits[i] = sum % 10

        if carry:
            return [1] + digits
        
        return digits
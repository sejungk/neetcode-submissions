class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1 # ways to reach step 0
        curr = 1 # ways to reach step 1

        for i in range(n-1):
            temp = prev
            prev = curr
            curr = temp + prev
        
        return curr
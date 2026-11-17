class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def fib(i):
            if i in memo:
                return memo[i]

            memo[i] = fib(i - 1) + fib(i - 2) + fib(i - 3)
            return memo[i]
            
        return fib(n)